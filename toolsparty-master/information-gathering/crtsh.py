#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2017-11-03

import re
import sys
import requests


def run(url, results=[]):
    _ = requests.get(url, timeout=15)
    text = _.text
    result = re.findall('DNS:\*\.(.*?)<BR>', text)
    for x in result:
        if x not in results:
            results.append(x)
            print(x)


if __name__ == "__main__":
    base, param = 'https://crt.sh/', '?q='
    domain = 'example.com' if len(sys.argv) != 2 else sys.argv[1]
    try:
        r = requests.session()
        req = r.get(base + param + domain)
        matches = re.findall('<TD style="text-align:center"><A href="(.*?)">', req.text)
    except Exception as e:
        matches = "None"
        exit(e.message)

    print("[+] Searching domains about: [%s] by https://crt.sh" % domain)
    domains = [base + p for p in matches]

    for d in domains:
        try:
            run(d)
        except:
            try:
                run(d)
            except Exception as e:
                print('[-] Request:[%s] error. Reason: %s' % (d, e.message))

    print("[+] Finshed")
