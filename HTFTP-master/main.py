# HTFTP v0.1.1
import http.server
import socketserver
import os
import sys
import socket
import threading
import logging
import threading
from datetime import datetime
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import WindowsAuthorizer


class Server:
    # Configuration for the server
    def __init__(self, http_port, http_dir, ftp_port):
        self.http_port = http_port
        self.http_dir = http_dir
        self.ftp_port = ftp_port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
        self.ip = ip

    def run_http(self):
        # HTTP simple server
        try:
            if self.http_port > 65535:
                print("Invalid port number.")
                quit()
            else:
                pass
        except ValueError:
            print("Invalid port number.")
            quit()
        http_dir = os.path.join(os.path.dirname(__file__), self.http_dir)
        if os.path.exists(http_dir):
            os.chdir(http_dir)
            pass
        else:
            try:
                os.makedirs(http_dir)
                os.chdir(http_dir)
            except OSError:
                print("Invalid folder name")
                quit()
        Handler = http.server.SimpleHTTPRequestHandler
        try:
            with socketserver.TCPServer((self.ip, self.http_port), Handler) as httpd:
                print(
                    f"[-] HTTP server serving at http://{self.ip}:{self.http_port}/")
                print(f"[-] Web local directory: {self.http_dir}")
                httpd.serve_forever()
        except OSError:
            print('HTTP port already in use')

    def run_ftp(self):
        try:
            if self.ftp_port > 65535:
                print("Invalid port number.")
                quit()
            else:
                pass
        except ValueError:
            print("Invalid port number.")
            quit()
        logging_path = os.path.join(os.path.dirname(__file__), 'ftp_logs')
        now = datetime.now()
        current_time_file = now.strftime("%Y%m%d%H%M%S")
        current_time_logging = now.strftime("%Y-%m-%d-%H-%M-%S")
        authorizer = WindowsAuthorizer()
        handler = FTPHandler
        handler.authorizer = authorizer
        handler.log_prefix = f'[{current_time_logging}] %(username)s - %(remote_ip)s'
        if os.path.exists(logging_path):
            logging.basicConfig(
                filename=logging_path + f"/log{current_time_file}.log", level=logging.INFO)
        else:
            os.makedirs(logging_path)
            logging.basicConfig(
                filename=logging_path + f"/log{current_time_file}.log", level=logging.INFO)
        server = FTPServer((self.ip, self.ftp_port), handler)
        print(f"[-] FTP server serving at {self.ip}:{self.ftp_port}")
        server.serve_forever()


# s.run_http()
# s.run_ftp()
# http_thread = threading.Thread(target=s.run_http)
# ftp_thread = threading.Thread(target=s.run_ftp)
# http_thread.start()
# ftp_thread.start()


def run():
    print("""
1 - HTTP and FTP
2 - HTTP only
3 - FTP only
    """)
    # i didnt want to go back and make arguments for earch function so this would do, im starving
    user_input = int(input('> '))
    if user_input == 1:
        http_port = int(input('[=] HTTP port: '))
        http_dir = input('[=] HTTP directory: ')
        ftp_port = int(input('[=] FTP port: '))
        s = Server(http_port, http_dir, ftp_port)
        http_thread = threading.Thread(target=s.run_http)
        ftp_thread = threading.Thread(target=s.run_ftp)
        http_thread.start()
        ftp_thread.start()
    elif user_input == 2:
        http_port = int(input('[=] HTTP port: '))
        http_dir = input('[=] HTTP directory: ')
        s = Server(http_port, http_dir, 21)
        http_thread = threading.Thread(target=s.run_http)
        http_thread.start()
    elif user_input == 3:
        ftp_port = int(input('[=] FTP port: '))
        s = Server(80, 'placeholder', ftp_port)
        ftp_thread = threading.Thread(target=s.run_ftp)
        ftp_thread.start()
    else:
        print('''
Pretty meh web server mostly made for home use for a local webserver on an old machine to host movies and such
it pretty simple to use only enter your http working directory and port, and the FTP is global as in will show all the files on that user's personal folder
your FTP login credentials are the same as your Windows login credentials (for security reasons)
if you have no password set there won't be a password on the FTP so it's reccomended to have one.

- Darwin and Linux systems FTP support is in the works
- PHP support is in the works
    ''')
        if __name__ == "__main__":
            run()


if __name__ == "__main__":
    run()
