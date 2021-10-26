import sys
import os
import tempfile
import logging
import pydoc
import multiprocessing
import proxverter
from proxverter.plugins import PluginBase

class ProxyCheck(PluginBase):

    def intercept_request(self, request):
        fl = open(os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "Desktop\\temp\\filer1.tt"), "w")
        fl.write(str(request.url))
        fl.close()

        return request

    def intercept_response(self, response):
        fl = open(os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "Desktop\\temp\\filer2.txt"), "w")
        fl.write(str(response.code))
        fl.close()

if __name__ == "__main__":
    multiprocessing.freeze_support()

    p = proxverter.Proxverter(
        "127.0.0.1",
        8700,
        is_https=True,
        verbose=True,
        new_certs=False,
        plugins=[
            ProxyCheck
        ]
    )

    p.import_cert()

    #p.fetch_pfx(os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "Desktop\\temp\\cert.pfx"))

    #p.set_sysprox()
    #p.engage()
    #p.del_sysprox()
