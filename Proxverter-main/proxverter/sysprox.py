import platform
import socket
import subprocess
import fileinput
import multiprocessing
import os
import re
import sys

class mac_proxy:
    '''
    Refers to the macos version of system wide proxy. Refer to `Proxy` class for initializing system wide proxy.
    '''

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port       = port

    def join(self):
        pass

class lin_proxy:
    '''
    Refers to the linux version of system wide proxy. Refer to `Proxy` class for initializing system wide proxy.
    '''

    def __init__(self, ip_address, port):
        globals()["pwd"] = __import__("pwd")
        self.aptconf    = '/etc/apt/apt.conf'
        self.envconf    = '/etc/environment'
        self.bashconf   = '/etc/bash.bashrc'
        self.wgetconf   = '/etc/wgetrc'
        self.ip_address = ip_address
        self.port       = str(port)

        out = subprocess.call("gsettings list-recursively org.gnome.system.proxy", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.gnome = True if not out else False
        if os.geteuid() != 0:
            raise OSError("This library requires root privileges")

        if not os.path.isfile(self.aptconf):
            fl = open(self.aptconf, 'w')
            fl.close()

    def set_env_vars(self):
        exists = False
        for line in fileinput.input(self.envconf, inplace=1):
            if "proxy" in line:
                exists = True
                line = re.sub(r'(.*)_proxy=(.*)', r'\1_proxy="\1://'+self.ip_address+':'+self.port+"/\"\n", line.rstrip())
            sys.stdout.write(line)

        if not exists:
            fl = open(self.envconf, "w")
            fl.write("PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games\"\n")
            fl.write("http_proxy=\"http://"+self.ip_address+":"+self.port+"/\"\n")
            fl.write("https_proxy=\"https://"+self.ip_address+":"+self.port+"/\"\n")
            fl.write("ftp_proxy=\"ftp://"+self.ip_address+":"+self.port+"/\"\n")
            fl.write("socks_proxy=\"socks://"+self.ip_address+":"+self.port+"/\"\n")
            fl.close()

    def set_apt_vars(self):
        exists = False
        for line in fileinput.input(self.aptconf, inplace=1):
            if "Acquire::" in line and "Cache" not in line:
                exists = True
                line = re.sub(r'Acquire::(.*)::proxy (.*)', r'Acquire::\1::proxy "\1://'+self.ip_address+":"+self.port+"/\";\n", line.rstrip())
            sys.stdout.write(line)

        if not exists:
            fl = open(self.aptconf, "w")
            fl.write("Acquire::http::proxy \"http://"+self.ip_address+":"+self.port+"/\";\n")
            fl.write("Acquire::https::proxy \"https://"+self.ip_address+":"+self.port+"/\";\n")
            fl.write("Acquire::ftp::proxy \"ftp://"+self.ip_address+":"+self.port+"/\";\n")
            fl.write("Acquire::http::No-Cache \"True\";\n")
            fl.write("Acquire::socks::proxy \"socks://"+self.ip_address+":"+self.port+"/\";\n")
            fl.close()

    def set_bash_vars(self):
        exists = False
        for line in fileinput.input(self.bashconf, inplace=1):
            if "export" in line:
                exists = True
                line = re.sub(r'export (.*)_proxy=(.*)', r'export \1_proxy=\1://'+self.ip_address+':'+self.port+'\n', line.rstrip())
            sys.stdout.write(line)

        if not exists:
            fl = open(self.bashconf, "r+")
            l  = fl.readlines()
            fl.close()

            fl = open(self.bashconf, "a")

            if not l[-1][-1]=='\n':
                fl.write("\n")

            fl.write("export http_proxy=http://"+self.ip_address+":"+self.port+"\n")
            fl.write("export https_proxy=https://"+self.ip_address+":"+self.port+"\n")
            fl.write("export ftp_proxy=ftp://"+self.ip_address+":"+self.port+"\n")
            fl.close()

    def set_wget_vars(self):
        exists = False
        for line in fileinput.input(self.wgetconf, inplace=1):
            if not line.startswith("#") and "proxy" in line:
                exists = True
                line = re.sub(r'(.*)_proxy=(.*)//(.*)', r'\1_proxy=\1://'+self.ip_address+':'+self.port+'\n', line.rstrip())
            sys.stdout.write(line)

        if not exists:
            fl = open(self.wgetconf, "r+")
            l  = fl.readlines()
            fl.close()

            fl = open(self.wgetconf, "a")
            if not l[-1][-1]=='\n':
                fl.write("\n")

            fl.write("http_proxy=http://"+self.ip_address+":"+self.port+"\n")
            fl.write("https_proxy=https://"+self.ip_address+":"+self.port+"\n")
            fl.write("ftp_proxy=ftp://"+self.ip_address+":"+self.port+"\n")

    def set_gsettings(self):
        def caller(ip_address, port, uid, gid, dhome, logname):
            os.setgid(gid)
            os.setuid(uid)
            os.environ['HOME']    = dhome
            os.environ['LOGNAME'] = logname

            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy mode 'manual'", shell=True)
            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy.http host '{ip_address}'", shell=True)
            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy.http port {port}", shell=True)
            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy.https host '{ip_address}'", shell=True)
            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy.https port {port}", shell=True)
            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy use-same-proxy true", shell=True)

        users = pwd.getpwall()
        for user in users:
            if hasattr(user, 'pw_name') and hasattr(user, 'pw_shell'):
                if (user.pw_shell == "/bin/bash" or user.pw_shell == "bin/sh"):
                    mp = multiprocessing.Process(target=caller, args=(self.ip_address, self.port, user.pw_uid, user.pw_gid, user.pw_dir, user.pw_name))
                    mp.daemon = True
                    mp.start()
                    mp.join()

    def rem_wget_vars(self):
        with open(self.wgetconf, "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "http_proxy" not in line and "https_proxy" not in line and "ftp_proxy" not in line and "socks_proxy" not in line:
                    f.write(line)
            f.truncate()
            f.close()

    def rem_bash_vars(self):
        with open(self.bashconf, "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "export http_proxy" not in line and "export https_proxy" not in line and "export ftp_proxy" not in line and "export socks_proxy" not in line:
                    f.write(line)
            f.truncate()
            f.close()

    def rem_env_vars(self):
        with open(self.envconf, "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "http_proxy" not in line and "https_proxy" not in line and "ftp_proxy" not in line and "socks_proxy" not in line:
                    f.write(line)
            f.truncate()
            f.close()

    def rem_apt_vars(self):
        with open(self.aptconf, "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "Acquire::http" not in line and "Acquire::https" not in line and "Acquire::ftp" not in line and "Acquire::socks" not in line:
                    f.write(line)
            f.truncate()
            f.close()

    def rem_gsettings(self):
        def caller(ip_address, port, uid, gid, dhome, logname):
            os.setgid(gid)
            os.setuid(uid)
            os.environ['HOME']    = dhome
            os.environ['LOGNAME'] = logname

            subprocess.call(f"dbus-launch gsettings set org.gnome.system.proxy mode 'none'", shell=True)

        users = pwd.getpwall()
        for user in users:
            if hasattr(user, 'pw_name') and hasattr(user, 'pw_shell'):
                if (user.pw_shell == "/bin/bash" or user.pw_shell == "bin/sh"):
                    mp = multiprocessing.Process(target=caller, args=(self.ip_address, self.port, user.pw_uid, user.pw_gid, user.pw_dir, user.pw_name))
                    mp.daemon = True
                    mp.start()
                    mp.join()

    def join(self):
        if self.gnome:
            self.set_gsettings()

        self.set_env_vars()
        self.set_apt_vars()
        self.set_bash_vars()
        self.set_wget_vars()

    def del_proxy(self):
        if self.gnome:
            self.rem_gsettings()

        self.rem_wget_vars()
        self.rem_bash_vars()
        self.rem_apt_vars()
        self.rem_env_vars()

class win_proxy:
    '''
    Refers to the windows version of system wide proxy. Refer to `Proxy` class for initializing system wide proxy.
    '''

    def __init__(self, ip_address, port):
        self.glob_import('winreg')
        self.glob_import('ctypes')

        self.regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_ALL_ACCESS)
        self.internet_option_refresh = 37
        self.internet_option_settings_changed = 39
        self.internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

        self.ip_address = ip_address
        self.port      = port

    def glob_import(self, module_name):
        globals()[module_name] = __import__(module_name)

    def refresh(self):
        self.internet_set_option(0, self.internet_option_settings_changed, 0, 0)
        self.internet_set_option(0, self.internet_option_refresh, 0, 0)

    def set_key(self, name, value):
        try:
            _, reg_type = winreg.QueryValueEx(self.regkey, name)
            winreg.SetValueEx(self.regkey, name, 0, reg_type, value)
        except FileNotFoundError:
            winreg.SetValueEx(self.regkey, name, 0, winreg.REG_SZ, value)

    def set_proxy(self):
        try:
            self.set_key('ProxyEnable', 1)
            #self.set_key('ProxyOverride', u'*.local;<local>')
            self.set_key('ProxyServer', u'%s:%i' % (self.ip_address, self.port))
            return True
        except IndexError:
            raise ValueError(f"Unable to find the registry path for proxy")
            return False

    def del_proxy(self):
        try:
            self.set_key('ProxyEnable', 0)
        except FileNotFoundError:
            pass

    def join(self):
        if not self.set_proxy():
            raise ValueError(f"Error setting proxy credentials")

        self.refresh()

class Proxy:

    ## Gets necessary information and kill mitmproxy if already running
    def __init__(self, ip_address, port):
        '''
            Accepts two arguments:

            ip_address: The IP address for system wide proxy
            port: The port for system wide proxy
        '''
        self.ip_address = ip_address
        self.port = port

    def get_prox_instance(self):
        plat = platform.system().lower()
        if plat == "windows":
            prox = win_proxy(self.ip_address, self.port)
        elif plat == "linux":
            prox = lin_proxy(self.ip_address, self.port)
        elif plat == "macos":
            prox = mac_proxy(self.ip_address, self.port)
        else:
            raise OSError("Unable to determine the underlying operating system")

        return prox

    def engage(self):
        '''
            Setup system wide proxy.
        '''

        prox = self.get_prox_instance()
        prox.join()

    def cleanup(self):
        '''
            Removes system wide proxy
        '''

        prox = self.get_prox_instance()
        prox.del_proxy()

        if hasattr(prox, 'refresh'):
            prox.refresh()
