import sys
import socket
import proxy
import tempfile
import shutil
import ipaddress
import os
import socket
import pathlib
import logging
import multiprocessing

## Package Imports
from . import installer
from . import certgen
from . import sysprox as sprox

class Proxverter:
    '''
    The main Proxverter class that accepts creds, setup system wide caches and run proxy servers.
    '''

    def __init__(self, ip, port, is_https=False, new_certs=False, sysprox=False, verbose=False, log_file=None, plugins=[]):
        self.ip_address = ip
        self.port       = port
        self.is_https   = is_https
        self.new_certs  = new_certs
        self.sysprox    = sysprox
        self.verbose    = verbose
        self.plugins    = plugins
        self.inargs     = []
        self.home_paths = self.__fetch_home_paths()
        self.proxy      = sprox.Proxy(self.ip_address, self.port)
        self.__check_connection()

        if self.is_https:
            self.__gen_certs()

        if self.sysprox:
            self.set_sysprox()

        if not self.verbose:
            logging.disable(logging.CRITICAL)

        if log_file:
            self.inargs.append('--log-file')
            self.inargs.append(log_file)

    def __check_connection(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(( self.ip_address, self.port ))
            s.close()
            return True
        except Exception as e:
            return False

    def __fetch_home_paths(self):
        dirname = os.path.join(pathlib.Path.home(), ".proxverter")
        rtval = {
            'dirname': dirname,
            'certname': os.path.join(dirname, "cert.pem"),
            'privname': os.path.join(dirname, "priv.pem"),
            'pfxname': os.path.join(dirname, "cert.pfx")
        }

        if not os.path.isdir(rtval['dirname']):
            os.makedirs(rtval['dirname'])

        return rtval

    def __gen_certs(self):
        if not os.path.isfile(self.home_paths['certname']) \
           or not os.path.isfile(self.home_paths['privname']) \
           or not os.path.isfile(self.home_paths['pfxname']) \
           or self.new_certs:

           gen = certgen.Generator()
           gen.generate()
           gen.gen_key(self.home_paths['privname'])
           gen.gen_cert(self.home_paths['certname'])
           gen.gen_pfx(self.home_paths['pfxname'])

    def __clear(self):
        try:
            shutil.rmtree(
                os.path.join(pathlib.Path.home(), ".proxy")
            )
        except FileNotFoundError:
            pass

    def set_sysprox(self):
        self.proxy.engage()

    def del_sysprox(self):
        self.proxy.cleanup()

    def fetch_pkey(self, destination):
        if not self.is_https:
            raise ValueError("Private keys are only implemented in SSL Mode")

        if not os.path.isfile(self.home_paths['privname']):
            raise FileNotFoundError("No private key file was found in home directory. It has either been modified or deleted. ")

        shutil.copyfile(self.home_paths['privname'], destination)

    def fetch_cert(self, destination):
        if not self.is_https:
            raise ValueError("Certificates are only implemented in SSL Mode")

        if not os.path.isfile(self.home_paths['certname']):
            raise FileNotFoundError("No cert file was found in home directory. It has either been modified or deleted. ")

        shutil.copyfile(self.home_paths['certname'], destination)

    def fetch_pfx(self, destination):
        if not self.is_https:
            raise ValueError("PFXs are only implemented in SSL Mode")

        if not os.path.isfile(self.home_paths['pfxname']):
            raise FileNotFoundError("No pfx file was found in home directory. It has either been modified or deleted. ")

        shutil.copyfile(self.home_paths['pfxname'], destination)

    def import_cert(self):
        if not self.is_https:
            raise ValueError("PFXs are only implemented in SSL Mode")

        imp = certgen.Importer(self.home_paths)
        return imp.cimport()

    def engage(self, certfile=None, privfile=None):
        self.__clear()

        try:
            if not self.is_https:
                proxy.main(
                    self.inargs,
                    hostname = ipaddress.IPv4Address(self.ip_address),
                    port = self.port,
                    num_workers=1,
                    plugins = self.plugins
                )
            else:
                if not certfile or not privfile:
                    if not os.path.isfile(self.home_paths['privname']):
                        raise FileNotFoundError("Given private key file doesn't exists")

                    if not os.path.isfile(self.home_paths['certname']):
                        raise FileNotFoundError("Given certificate file doesn't exists")
                else:
                    if not os.path.isfile(certfile):
                        raise FileNotFoundError("Given private key file doesn't exists")

                    if not os.path.isfile(privfile):
                        raise FileNotFoundError("Given certificate file doesn't exists")

                proxy.main(
                    self.inargs,
                    hostname = ipaddress.IPv4Address(self.ip_address),
                    port = self.port,
                    num_workers=1,
                    ca_key_file = self.home_paths['privname'] if not privfile else privfile,
                    ca_cert_file = self.home_paths['certname'] if not certfile else certfile,
                    ca_signing_key_file = self.home_paths['privname'] if not privfile else privfile,
                    plugins = self.plugins
                )

        except KeyboardInterrupt:
            pass

        if self.sysprox:
            self.del_sysprox()
