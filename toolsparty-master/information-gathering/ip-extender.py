#!/usr/bin/env python
# coding: utf-8
# -**- Author: LandGrey -**-

import os
import sys


def ip_extender(ips=None, files=None, switch=3, extend=5, is_format=False):
    results = []
    cidr_groups = []
    none_cidr_groups = []
    cidr_dict = {}
    if not ips and files:
        ips = []
        with open(files, 'r') as f:
            for line in f.readlines():
                if line.strip():
                    ips.append(line.strip())
    ips = list(set(ips))

    for ip in ips:
        prefix = ".".join(ip.split(".")[:3])
        if prefix not in cidr_dict.keys():
            cidr_dict[prefix] = [1, ip]
        else:
            cidr_dict[prefix][0] += 1
            cidr_dict[prefix].append(ip)

    for k, v in cidr_dict.items():
        if v[0] >= switch:
            cidr_groups.append(k)
        else:
            for _ in v[1:]:
                none_cidr_groups.append(_)
    if not is_format:
        for _ in cidr_groups:
            results.extend(extend_ips([_ + ".128"]))
        results.extend(extend_ips(none_cidr_groups, extend=extend))
    else:
        for _ in cidr_groups:
            results.append(_ + ".0/24")
        for _ in none_cidr_groups:
            r = extend_ips([_], extend=extend)
            results.append(r[0] + "-" + r[-1])
    return results


def extend_ips(ips, extend=128):
    results = ips
    var0 = []
    for ip in ips:
        ip_chunk = ip.split(".")
        for chunk in range(min(int(ip_chunk[3]) - int(extend), int(ip_chunk[3]) - 1)
                           if int(ip_chunk[3]) - int(extend) > 0 else 1, min(int(ip_chunk[3]) + int(extend) + 1, 256)):
            var0.append("{0}.{1}.{2}.{3}".format(ip_chunk[0], ip_chunk[1], ip_chunk[2], str(chunk)))
    results.extend(var0)
    return sorted(list(set(results)), key=lambda x: (len(x), str(x)))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        exit("[*] Usage: python ip-extender.py single_ip_list.txt")
    for ip in ip_extender(files=sys.argv[1], is_format=True):
        print(ip)
