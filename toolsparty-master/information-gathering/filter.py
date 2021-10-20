#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2017-11-04

import os
import re
import sys
import itertools
from netaddr import IPNetwork


def unique(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    results = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        results.append(item)
    return results


def get_subdir_path(directory, only_file_path=True):
    dirpaths = []
    filepaths = []
    for rootpath, subdirsname, filenames in os.walk(directory):
        dirpaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in subdirsname])
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])
    if only_file_path:
        return filepaths
    else:
        return dirpaths, filepaths


def walk_all_files(directory):
    contents = []
    for _ in get_subdir_path(directory):
        with open(_, 'r') as f:
            for line in f.readlines():
                if line.strip() != '':
                    contents.append(line.strip())
    return unique(contents)


def rematch(line, limit=False):
    mail_matches = mail_pattern.findall(line)
    mails.extend([mm[0] for mm in mail_matches] if not limit else [d[0] for d in mail_matches if d[0].endswith(limit)])
    domain_matches = domain_pattern.findall(line)
    domains.extend([dm[0] for dm in domain_matches] if not limit else [d[0] for d in domain_matches if d[0].endswith(limit)])
    internal_ip_matches = internal_ip_pattern.findall(line)
    if internal_ip_matches:
        internal_ip.extend([y for x in internal_ip_matches for y in x if len(y) >= 7 and y.split('.')[0]])
    else:
        external_ip_matches = common_ip_pattern.findall(line)
        external_ip.extend([y for x in external_ip_matches for y in x if len(y) >= 7 and y.split('.')[0]])


def ip_handler(collections):
    targets_pool = []
    for ipstring in collections:
        if ipstring.startswith("http"):
            ipstring = ((ipstring.strip()).split("/")[2]).split(":")[0]
        else:
            ipstring = (ipstring.strip()).split(":")[0]
        t_dic = {1: [], 2: [], 3: [], 4: []}
        if "-" not in ipstring and "/" not in ipstring:
            targets_pool.append(ipstring)
        elif "-" in ipstring:
            sc_chunk = ipstring.split(".")
            if len(sc_chunk) != 4:
                exit("[-] Target Error\n")
            else:
                for r in range(0, 4):
                    if "-" in sc_chunk[r]:
                        sc_chunk_split = sc_chunk[r].split("-")
                        if not (len(sc_chunk_split) == 2 and sc_chunk_split[0].isdigit()
                                and sc_chunk_split[1].isdigit() and int(sc_chunk_split[0]) <= int(sc_chunk_split[1])
                                and 0 <= int(sc_chunk_split[0]) <= 255 and 0 <= int(sc_chunk_split[1]) <= 255):
                            exit("[-] range error: %s\n" % ipstring)
                        else:
                            if len(sc_chunk_split) == 1:
                                t_dic[r + 1].append(sc_chunk[0])
                            for _ in range(int(sc_chunk_split[0]), int(sc_chunk_split[1]) + 1):
                                t_dic[r + 1].append(_)
                    else:
                        if not (sc_chunk[r].isdigit() and 0 <= int(sc_chunk[r]) <= 255):
                            exit("[-] ip address error: %s\n" % ipstring)
                        t_dic[r + 1].append(sc_chunk[r])
            for item in itertools.product(t_dic[1], t_dic[2], t_dic[3], t_dic[4]):
                targets_pool.append(
                    "{0}.{1}.{2}.{3}".format(str(item[0]), str(item[1]), str(item[2]), str(item[3])))
        elif "/" in ipstring:
            for _ in list(IPNetwork(ipstring)):
                targets_pool.append(_)
    return targets_pool


if __name__ == "__main__":
    if not (len(sys.argv) == 2 or len(sys.argv) == 3):
        exit("[*] python filter.py file_or_dir [domain_limit]")
    if len(sys.argv) == 2:
        strict = False
    else:
        strict = sys.argv[2]

    mails = []
    domains = []
    internal_ip = []
    external_ip = []

    ip_pattern = re.compile(r'(\d{1,3}[.])(\d{1,3}[.])(\d{1,3}[.])(\d{1,3})')
    common_ip_pattern = re.compile('((\d{1,3}(-?\d{1,3})?\.){3}\d{1,3}(/?-?\d{1,3})?((\.\d{1,3}){3})?)')
    domain_pattern = re.compile('((((\d|\w|-)*)\.)+[a-zA_Z]{2,})')
    mail_pattern = re.compile('(.*?@((((\d|\w|-)*)\.)+[a-zA_Z]{2,}))')
    internal_ip_pattern = re.compile(r'(10\.(\d{1,3}(-?\d{1,3})?\.){2}\d{1,3}(/?-?\d{1,3})?((\.\d{1,3}){3})?)|'
                                     r'(127\.(\d{1,3}(-?\d{1,3})?\.){2}\d{1,3}(/?-?\d{1,3})?((\.\d{1,3}){3})?)|'
                                     r'(172\.(1[6-9]|2[0-9]|3[0-1])\.(\d{1,3}(-?\d{1,3})?\.)+\d{1,3}(/?-?\d{1,3})?((\.\d{1,3}){3})?)|'
                                     r'(192\.168\.(\d{1,3}(-?\d{1,3})?\.)+\d{1,3}(/?-?\d{1,3})?((\.\d{1,3}){3})?)')

    if os.path.isdir(sys.argv[1]):
        for row in walk_all_files(sys.argv[1]):
            rematch(row, strict)
    elif os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            for row in f.readlines():
                rematch(row.strip(), strict)
    final_internal_ip = unique(ip_handler(internal_ip))
    final_external_ip = unique(ip_handler(external_ip))

    print("[+]        mails       (%s)" % len(unique(mails)))
    for m in unique(mails):
        print(m)
    print("\n[+]        domains     (%s)" % len(unique(domains)))
    for d in unique(domains):
        print(d)
    print("\n[+]        internal ip (%s)" % len(final_internal_ip))
    for ip in final_internal_ip:
        print(ip)
    print("\n[+]        external ip (%s)" % len(final_external_ip))
    for ip in final_external_ip:
        print(ip)
