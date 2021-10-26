import subprocess
import os
import platform

class Installer:

    def __init__(self, output=os.devnull):
        self.chocoline = 'Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))'
        self.chocolime = 'choco install {} -y'
        self.aptline   = 'apt update'
        self.aptlime   = 'apt install {}'
        self.platform  = platform.system().lower()
        if self.platform == "windows":
            self.startupinfo = subprocess.STARTUPINFO()
            self.startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self.output    = output

    def activate(self):
        lpoint = os.environ.get("COMSPEC", None)
        fl = open(self.output, 'w')
        if hasattr(self, 'startupinfo'):
            os.environ["COMSPEC"] = "powershell"
            cmline = subprocess.Popen(
                self.chocoline,
                shell=True,
                stdin=subprocess.PIPE,
                stdout=fl,
                stderr=fl,
                startupinfo=self.startupinfo
            )
        else:
            cmline = subprocess.Popen(
                self.aptline,
                shell=True,
                stdin=subprocess.PIPE,
                stdout=fl,
                stderr=fl
            )

        try:
            cmline.communicate(timeout=60)
        except subprocess.TimeoutExpired:
            return False
        finally:
            fl.close()
            os.environ["COMSPEC"] = lpoint

        if cmline.returncode:
            raise ImportError(f"Unable to activate environment installer. Return code: {cmline}")

        return cmline.returncode == 0

    def install(self, pkg):
        lpoint = os.environ.get("COMSPEC", None)
        fl = open(self.output, 'a')
        if hasattr(self, 'startupinfo'):
            os.environ["COMSPEC"] = "powershell"
            cmline = subprocess.Popen(
                self.chocolime.format(pkg),
                shell=True,
                stdin=subprocess.PIPE,
                stdout=fl,
                stderr=fl,
                startupinfo=self.startupinfo
            )
        else:
            cmline = subprocess.Popen(
                self.aptlime.format(pkg),
                shell=True,
                stdin=subprocess.PIPE,
                stdout=fl,
                stderr=fl
            )
        cmline.communicate()
        fl.close()
        os.environ["COMSPEC"] = lpoint

        if cmline.returncode:
            raise ImportError(f"Unable to install {pkg}. Return code: {cmline}")

        return cmline.returncode == 0
