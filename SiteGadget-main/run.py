#https://github.com/alpkeskin
import socket, requests, json, urllib3, dns, dns.resolver, sys
from insides.Colors import Colors
from insides.Banner import Banner
from insides.Header import Header
##############BANNER################
Banner()
####################################
###########CONFIG FILE##############
configfile = open('config.json', "r")
config = json.loads(configfile.read())
for i in config:
	conftree = (i['Tree'])
	confdns = (i['DNS Lookup'])
	confhttp = (i['HTTP Headers'])
	confReverseIP = (i['Reverse IP Lookup'])
	confCMS = (i['whatcms.org API'])
	confHunter = (i['hunter.io API'])
	confscraping = (i['Scraping The Links'])
	confportscan = (i['Port Scan'])
	confFindAP = (i['Find Admin Panel'])
	confFindShell = (i['Find Shell'])
####################################
##############INPUTs################
inp = input(f"{Colors.HEADER}SITE >{Colors.ENDC}")
if (inp == "q" or inp == "Q" or inp == "exit"):
	print("See u inspector :)")
	sys.exit(0)
elif(inp.find(".") == -1):
	print(f"{Colors.WARNING}Wrong input!{Colors.ENDC}")
	sys.exit(0)
site = inp.lower()
getip =(socket.gethostbyname(site)) # GET IP 
####################################
############## TREE ################
if (conftree == "True" or conftree == "true"):
	from modules.Tree import Tree
	Tree(site,getip,_verbose=True)
	print("")
####################################
########### DNS LOOKUP #############
if (confdns == "True" or confdns == "true"):
	from modules.DNSLookup import DNSLookup
	title = "DNS LOOKUP"
	Header(title)
	DNSLookup(site,_verbose=True)
####################################
######## REVERSE IP LOOKUP #########
if (confReverseIP == "True" or confReverseIP == "true"):
	from modules.ReverseIP import ReverseIP
	title = "REVERSE IP LOOKUP"
	Header(title)
	ReverseIP(site,_verbose=True)
####################################
########## HTTP HEADERS ############
if (confhttp == "True" or confhttp == "true"):
	from modules.HTTPHeaders import HTTPHeaders
	title = "HTTP HEADERS"
	Header(title)
	http = urllib3.PoolManager()
	r = http.request('GET', "https://"+site)
	HTTPHeaders(site,r, _verbose=True)
####################################
########### DETECT CMS #############
if (confCMS != ""):
	from modules.DetectCMS import DetectCMS
	title = "Detecting CMS & Technologies..."
	Header(title)
	DetectCMS(confCMS,site, _verbose=True)
####################################
######### RELATED EMAILS ##########
if (confHunter != ""):
	from modules.Hunter import Hunter
	title = "RELATED EMAILS"
	Header(title)
	Hunter(site,confHunter, _verbose=True)
####################################
######## SCRAPING THE LINKS ########
if (confscraping == "True" or confscraping == "true"):
	from modules.Scraping import Scraping
	title = "Scraping The Links..."
	Header(title)
	Scraping(site, _verbose=True)
####################################
############ PORT SCAN #############
if (confportscan == "True" or confportscan == "true"):
	from modules.PortScan import PortScan
	title = "Scanning Ports..."
	Header(title)
	PortScan(getip, _verbose=True)
####################################
######### FIND ADMIN PANEL #########
if (confFindAP == "True" or confFindAP == "true"):
	from modules.findAdminPanel import findAdminPanel
	title = "Finding Admin Panel..."
	Header(title)
	findAdminPanel(site, _verbose=True)
####################################
######### FIND SHELL PANEL #########
if (confFindShell == "True" or confFindShell == "true"):
	from modules.findShell import findShell
	title = "Finding Shell..."
	Header(title)
	findShell(site, _verbose=True)
####################################
