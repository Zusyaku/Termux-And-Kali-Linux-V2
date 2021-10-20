#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# vulners-lookup
# --------------
# Perform vulnerabilities lookup on Vulners, the largest database (lots of sources
# including exploit-db, 0day.today, Nessus, OpenVAS...). Ref: https://vulners.com/stats
#
# Based on Vulners API (https://github.com/vulnersCom/api)
#
# TODO:
# ----
# - Find a way to handle this problem when too much results:
# $ python3 vulners-lookup.py software --cpe 'cpe:/a:oracle:database_server' --version 11.2.0.3
# [*] Querying Vulners API for: cpe="cpe:/a:oracle:database_server", version=11.2.0.3...
# [!] Vulners API returns 0 result
# {
#   "result": "warning",
#   "data": {
#     "warning": "Too much results - 70 for the query (cpe:\"cpe:/a:oracle:database_server\" AND (cpe:11.2.0.3* OR (description:\"11.2.0.3\" AND NOT (\"before version 11.2.0.3\" OR \"< 11.2.0.3\" OR \"less than 11.2.0.3\" OR \"before 11.2.0.3\" OR \"prior to 11.2.0.3\")))) OR (description:\"database_server\" AND description:\"11.2.0.3\" AND title:\"database_server\" AND bulletinFamily:exploit AND NOT (\"before version 11.2.0.3\" OR \"< 11.2.0.3\" OR \"less than 11.2.0.3\" OR \"before 11.2.0.3\" OR \"prior to 11.2.0.3\") AND -type:seebug) with software:cpe:/a:oracle:database_server version:11.2.0.3",
#     "errorCode": 402
#   }
# }

import argparse
import requests
import vulners
import pprint
import colored
import prettytable
import textwrap
import sys


# Utils functions
# -----------------------------------------------------------------------------
def colorize(string, color=None, highlight=None, attrs=None):
    """Apply style on a string"""
    # Colors list: https://pypi.org/project/colored/
    return colored.stylize(
        string,
        (colored.fg(color) if color else "")
        + (colored.bg(highlight) if highlight else "")
        + (colored.attr(attrs) if attrs else ""),
    )


def remove_non_printable_chars(string):
    """Remove non-ASCII chars like chinese chars"""
    printable = set(
        """0123456789abcdefghijklmnopqrstuvwxyz"""
        """ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    )
    return "".join(filter(lambda x: x in printable, string))


def table(columns, data, hrules=True):
    """Print a table"""
    columns = map(lambda x: colorize(x, attrs="bold"), columns)
    table = prettytable.PrettyTable(
        hrules=prettytable.ALL if hrules else prettytable.FRAME, field_names=columns
    )
    for row in data:
        table.add_row(row)
    table.align = "l"
    print(table)


def shorten(string, maxlength):
    """Shorten a string if it exceeds a given length"""
    if len(string) <= maxlength:
        return string
    else:
        return textwrap.wrap(string, maxlength)[0] + "..."


def get_cvss_score(vuln, vulners_api):
    """Get CVSS score if available, otherwise get Vulners AI score"""
    cvss = vuln["cvss"]["score"]

    if cvss == 0.0:
        try:
            return vulners_api.aiScore(vuln["description"])[0]
        except:
            return 0.0
    else:
        return cvss


def color_cvss(cvss):
    """Attribute a color to the CVSS score"""
    try:
        cvss = float(cvss)
    except:
        return None

    if cvss < 3:
        color = "green_3b"
    elif cvss <= 5:
        color = "yellow_1"
    elif cvss <= 7:
        color = "orange_1"
    elif cvss <= 8.5:
        color = "dark_orange"
    else:
        color = "red"
    return color


def info(string):
    """Print info string"""
    print("{}{}".format(colorize("[*] ", color="light_blue", attrs="bold"), string))


def warning(string):
    """Print warning string"""
    print("{}{}".format(colorize("[!] ", color="orange_1", attrs="bold"), string))


def error(string):
    """Print error string"""
    print("{}{}".format(colorize("[!] ", color="red", attrs="bold"), string))


def global_search(apikey, query):
    info('Looking for "{}" in whole Vulners database...'.format(query))

    try:
        vulners_api = vulners.Vulners(api_key=apikey)
    except:
        error("Unable to connect to Vulners.com. No Internet connection "
            "or maximum requests count has been reached with the API key")
        sys.exit(1)

    try:
        results = vulners_api.search("{}  order:published".format(query), limit=200)
    except Exception as e:
        error(
            "Unable to get results. Might happen is maximum requests count has been "
            "reached with the API key in use"
        )
        sys.exit(1)

    nb_results = 0
    excluded_families = ("info", "blog", "bugbounty", "tools", "advertisement")

    for r in results:
        if r["bulletinFamily"] not in excluded_families:
            nb_results += 1

    if nb_results == 0:
        warning("No result has been found !")
        sys.exit(0)
    else:
        info(
            "{} results found. Retrieving CVSS scores or computing AI scores if "
            "not available...".format(nb_results)
        )

    i = 1
    filtered_results = []
    for r in results:
        if r["bulletinFamily"] not in excluded_families:
            score = get_cvss_score(r, vulners_api)
            type_ = r["bulletinFamily"]

            result = {
                "reference": r["id"],
                "score": score,
                "title": remove_non_printable_chars(r["title"]).replace(";", ","),
                "description": remove_non_printable_chars(r["description"]).replace(
                    ";", ","
                ),
                "url": r["vhref"],
                "type": type_,
            }
            filtered_results.append(result)
            i += 1

    return filtered_results


def software_api(mode, software, version):
    """
    Query Vulners API in software mode. Same API used by:
        - https://github.com/vulnersCom/nmap-vulners
        - https://github.com/vulnersCom/burp-vulners-scanner

    :param str mode: Mode to use - either "cpe" or "software". 
        According to tests, "cpe" gives better results
    :param str software: CPE v2.2 (without version) in "cpe" mode, product name in 
        "software" mode
    :param str version: Version number
    """
    info(
        'Querying Vulners API for: {mode}="{name}", version={version}...'.format(
            mode='cpe' if mode == 'cpe' else 'name',
            name=software, 
            version=version
        )
    )

    try:
        res = requests.get(
            "https://vulners.com/api/v3/burp/software",
            params={"software": software, "version": version, "type": mode},
        )
    except:
        error("Unable to query the Vulners API. Check Internet Connection !")
        sys.exit(1)

    if not res:
        error("Empty result returned by Vulners API")
        sys.exit(1)

    try:
        json = res.json()
    except:
        error(
            "Response from Vulners endpoint is not valid JSON data. Cannot process it !"
        )
        sys.exit(1)

    # Empty result :
    # {
    #   "result": "warning",
    #   "data": {
    #     "warning": "Nothing found for Burpsuite search request",
    #     "errorCode": 401
    #   }
    # }
    results = []
    if json["result"] == "OK":
        for res in json["data"]["search"]:
            result = {
                "reference": res["_id"],
                "score": res["_source"]["cvss"]["score"]
                if "cvss" in res["_source"] and "score" in res["_source"]["cvss"]
                else None,
                "title": remove_non_printable_chars(res["_source"]["title"]).replace(
                    ";", ","
                ),
                "description": remove_non_printable_chars(
                    res["_source"]["description"]
                ).replace(";", ","),
                "url": res["_source"]["href"],
                "type": res["_source"]["type"],
            }
            if result["score"] == 0.0:
                result["score"] = None

            results.append(result)

    else:
        warning("Vulners API returns 0 result")
        if json["data"]["errorCode"] != 401:
            print(res.text)
        sys.exit(0)

    return results


def display_results(results):
    columns = ["#", "Score", "Title", "Description", "URL", "Type"]
    data = list()
    for r in results:
        data.append(
            [
                textwrap.fill(r["reference"], 20),
                colorize(r["score"], color=color_cvss(r["score"]), attrs="bold")
                if r["score"]
                else "",
                textwrap.fill(remove_non_printable_chars(r["title"]), 30),
                textwrap.fill(remove_non_printable_chars(r["description"]), 50),
                textwrap.fill(r["url"], 78),
                colorize(r["type"], color="red", attrs="bold")
                if r["type"] == "exploit"
                else r["type"],
            ]
        )

    # pprint.pprint(results)

    info("{} results returned:".format(len(results)))
    table(columns, data, hrules=True)


# Command-line parsing
# -----------------------------------------------------------------------------
# Examples:
# * Mode "all" (requires API key):
#     python3 vulners-lookup.py all --apikey <API-key> "Apache Tomcat 8.5.0"
#     python3 vulners-lookup.py --apikey <API-key> 'affectedSoftware.name:"Microsoft IIS"
#         AND affectedSoftware.version:"6.0"'
# * Mode "software":
# """

DESCRIPTION = """
Usage Examples:
---------------
- Global search (requires API key):
    python3 vulners-lookup.py all --apikey <API-key> 'Apache Tomcat 8.5.0'
    python3 vulners-lookup.py all --apikey <API-key> 'affectedSoftware.name:"Microsoft IIS" AND affectedSoftware.version:"6.0"'

- Software search (API used by Nmap vulners NSE script & Burp add-on):
    python3 vulners-lookup.py software --name proftpd --version 1.3
    python3 vulners-lookup.py software --cpe 'cpe:/a:joomla:joomla' --version 3.7
"""

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter, epilog=DESCRIPTION
)

parser.add_argument(
    "--csv",
    help="Output as CSV file (fields separated by semicolon)",
    action="store",
    metavar="<output-filename>",
    dest="csv",
)
parser.add_argument(
    "--display-csv",
    help="Display CSV data at the end",
    action="store_true",
    dest="displaycsv",
)

subparsers = parser.add_subparsers(dest="mode")

parser_all = subparsers.add_parser("all")
parser_all.add_argument(
    "--apikey",
    help="Vulners API key",
    action="store",
    dest="apikey",
    metavar="<API-key>",
    required=True,
    default=None,
)
parser_all.add_argument("query", help="Query", action="store")

parser_software = subparsers.add_parser("software")
parser_software.add_argument(
    "--name",
    help="Product name",
    action="store",
    dest="name",
    metavar="<name>",
)
parser_software.add_argument(
    "--cpe",
    help='Product CPE v2.2 (e.g. "cpe:/a:apache:tomcat")',
    action='store',
    dest='cpe',
    metavar='<cpe>',
)
parser_software.add_argument(
    "--version",
    help="Version number",
    action="store",
    dest="version",
    metavar="<version>",
    required=True,
)

args = parser.parse_args()


# Processing
# -----------------------------------------------------------------------------
if args.mode == "all":
    results = global_search(args.apikey, args.query)
elif args.mode == "software":
    if not args.name and not args.cpe:
        error('Wrong Usage: Either --name or --cpe is required')
        sys.exit(1)

    if args.cpe:
        results = software_api('cpe', args.cpe, args.version)
    else:
        results = software_api('software', args.name, args.version)
else:
    sys.exit(1)

results.sort(key=lambda x: x['score'] or 0, reverse=True)

display_results(results)

# pprint.pprint(results)
if args.csv or args.displaycsv:
    csvdata = "ID;CVSS;Title;Description;URL;Type\n"
    for r in results:
        csvdata += "{ref};{cvss};{title};{description};{url};{type}\n".format(
            ref=r["reference"],
            cvss=r["score"],
            title=r["title"],
            description=r["description"],
            url=r["url"],
            type=r["type"],
        )

    if args.displaycsv and len(results) > 0:
        print()
        info("CSV output:")
        print(csvdata)

    if args.csv:
        try:
            with open(args.csv, "w") as f:
                f.write(csvdata)

            info("CSV output written to {csv} file".format(csv=args.csv))
        except Exception as e:
            error("An error occured when trying to write CSV output: {exc}".format(exc=e))
