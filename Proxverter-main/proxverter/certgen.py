from OpenSSL import crypto, SSL
import OpenSSL
import random
import re
import os
import shutil
import platform
import subprocess

class Generator:

    def __init__(self, email=None, country=None, province=None, locality=None, organization=None, unit=None, commonname=None):
        self.email   = email
        self.country = country
        self.province = province
        self.locality = locality
        self.organization = organization
        self.unit     = unit
        self.commonname = commonname or "example.com"
        self.serial_number = random.getrandbits(64)
        self.valid_start = 0
        self.valid_end   = 10*365*24*60*60

    def generate(self):
        self.cert = crypto.X509()
        self.key = crypto.PKey()
        self.key.generate_key(crypto.TYPE_RSA, 2048)
        if self.country:
            self.cert.get_subject().C = self.country
        if self.province:
            self.cert.get_subject().ST = self.province
        if self.locality:
            self.cert.get_subject().L = self.locality
        if self.organization:
            self.cert.get_subject().O = self.organization
        if self.unit:
            self.cert.get_subject().OU = self.unit
        self.cert.get_subject().CN = self.commonname
        if self.email:
            self.cert.get_subject().emailAddress = self.email
        self.cert.set_serial_number(self.serial_number)
        self.cert.gmtime_adj_notBefore(self.valid_start)
        self.cert.gmtime_adj_notAfter(self.valid_end)
        self.cert.set_issuer(self.cert.get_subject())
        self.cert.set_pubkey(self.key)
        self.cert.sign(self.key, 'sha256')

    def gen_key(self, key_file):
        key_file = open(key_file, 'wt')
        try:
            key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, self.key).decode("utf-8"))
        except TypeError:
            key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, self.key))
        key_file.close()

    def gen_cert(self, cert_file):
        cert_file = open(cert_file, 'wt')
        try:
            cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, self.cert).decode("utf-8"))
        except TypeError:
            cert_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, self.key))
        cert_file.close()

    def gen_pfx(self, pfx_file):
        p12 = OpenSSL.crypto.PKCS12()
        p12.set_privatekey( self.key )
        p12.set_certificate( self.cert )

        pfx_file = open(pfx_file, 'wb')
        pfx_file.write(p12.export())
        pfx_file.close()

class Importer:

    def __init__(self, home_paths):
        self.home_paths = home_paths

        if not os.path.isfile(self.home_paths['privname']):
            raise FileNotFoundError("No private key file was found in home directory. It has either been modified or deleted. ")

        if not os.path.isfile(self.home_paths['certname']):
            raise FileNotFoundError("No cert file was found in home directory. It has either been modified or deleted. ")

        if not os.path.isfile(self.home_paths['pfxname']):
            raise FileNotFoundError("No pfx file was found in home directory. It has either been modified or deleted. ")

    def __config_wn_firefox(self):
        import winreg
        import ctypes

        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if not is_admin:
            raise PermissionError("Configuring firefox requires admin privileges")

        try:
            tkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\firefox.exe")
            path = winreg.QueryValueEx(tkey, 'Path')[0]
        except:
            return -1

        autoconfig = os.path.join(path, 'defaults/pref/autoconfig.js')
        proxconfig = os.path.join(path, 'proxverter.cfg')

        fl = open(autoconfig, 'w')
        fl.write('pref("general.config.filename", "proxverter.cfg");\n')
        fl.write('pref("general.config.obscure_value", 0);\n')
        fl.close()

        fl = open(proxconfig, 'w')
        fl.write('//\n')
        fl.write('lockPref("network.proxy.type", 5);\n')
        fl.write('lockPref("security.enterprise_roots.enabled", true);\n')
        fl.close()

    def __import_windows(self):
        import ctypes

        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if not is_admin:
            raise PermissionError("Importing certificate requires admin privileges")

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        comm = subprocess.check_output(
            'powershell.exe "Get-PfxCertificate -FilePath \'{}\'"'.format(self.home_paths['pfxname']),
            shell=True,
            startupinfo=startupinfo,
            stdin=subprocess.PIPE
        )

        thumbprint = comm.split(b"\r\n")[3].split(b" ")[0].decode()

        comm = subprocess.check_output(
            'powershell.exe "Test-Path (Join-Path Cert:\LocalMachine\Root\ {})"'.format(thumbprint),
            shell=True,
            startupinfo=startupinfo,
            stdin=subprocess.PIPE
        )

        if comm.strip() == b"False":
            comm = subprocess.call(
                'powershell.exe "Import-PfxCertificate -FilePath \'{}\' -CertStoreLocation \'cert:\LocalMachine\Root\\\'"'.format(self.home_paths['pfxname']),
                shell=True,
                startupinfo=startupinfo,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            if comm:
                raise SystemError("Error while importing certificate ")
            return 0
        else:
            return 1

    def __config_ln_firefox(self):
        if not os.path.isdir('/usr/lib/firefox/defaults'):
            return

        path      = "/usr/lib/firefox/"
        autoconfig = os.path.join(path, 'defaults/pref/autoconfig.js')
        proxconfig = os.path.join(path, 'proxverter.cfg')

        fl = open(autoconfig, 'w')
        fl.write('pref("general.config.filename", "proxverter.cfg");\n')
        fl.write('pref("general.config.obscure_value", 0);\n')
        fl.close()

        fl = open(proxconfig, 'w')
        fl.write('//\n')
        fl.write('lockPref("network.proxy.type", 5);\n')
        fl.write('lockPref("security.enterprise_roots.enabled", true);\n')
        fl.close()

    def __import_linux(self):
        globals()["pwd"] = __import__("pwd")
        shutil.copy(self.home_paths['certname'], f"/usr/local/share/ca-certificates/proxverter.crt")
        subprocess.call("chmod 777 /usr/local/share/ca-certificates/proxverter.crt", shell=True)
        subprocess.call("update-ca-certificates", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        users = pwd.getpwall()
        for user in users:
            if hasattr(user, 'pw_name') and hasattr(user, 'pw_shell'):
                if (user.pw_shell == "/bin/bash" or user.pw_shell == "bin/sh"):

                    ## For Chrome
                    if not os.path.isdir(os.path.join(user.pw_dir, ".pki/nssdb")):
                        os.makedirs(os.path.join(user.pw_dir, ".pki/nssdb"))
                    subprocess.call(f'certutil -d sql:{user.pw_dir}/.pki/nssdb -A -t "C,C,C" -n proxverter -i {self.home_paths["certname"]}', shell=True)

                    ## For Firefox
                    if os.path.isdir(os.path.join(user.pw_dir, ".mozilla/firefox")):
                        dirm = ""
                        for dd in os.listdir(os.path.join(user.pw_dir, ".mozilla/firefox")):
                            if dd.endswith("-release"):
                                dirm = dd
                                break

                        if dirm:
                            subprocess.call(f'certutil -d "sql:{user.pw_dir}/.mozilla/firefox/{dirm}" -A -t "C,C,C" -n proxverter -i {self.home_paths["certname"]}', shell=True)

        return 0

    def cimport(self):
        plat = platform.system().lower()
        if plat == "windows":
            rtval = self.__import_windows()
            self.__config_wn_firefox()
            return rtval
        elif plat == "linux":
            rtval = self.__import_linux()
            self.__config_ln_firefox()
            return rtval
        elif plat == "macos":
            pass
        else:
            raise OSError("Unable to determine the underlying operating system")
