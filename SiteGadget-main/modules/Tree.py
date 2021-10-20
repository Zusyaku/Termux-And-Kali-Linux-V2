import socket, requests, json, urllib3
from anytree import Node, RenderTree
from insides.Colors import Colors

def Tree(site,getip, _verbose=None):
	if _verbose != None:
		u = ("http://ip-api.com/json/"+getip)
		response = requests.get(u)
		text = response.content
		data = json.loads(text)

		u = ("https://www.threatcrowd.org/searchApi/v2/domain/report/?domain="+site)
		response = requests.get(u)
		text = response.content
		data2 = json.loads(text)

		tsite = Node(site)
		tgetip = Node(getip, parent=tsite)
		tcountry = Node(data['country'], parent=tgetip)
		tcity = Node(data['city'], parent=tgetip)
		ttimezone = Node(data['timezone'], parent=tgetip)
		temails = Node("Emails", parent=tsite)
		try:
			for x in range(len(data2['emails'])):
				x = Node(data2['emails'][x], parent=temails)
		except:
			pass
		tsubdomains = Node("Subdomains", parent=tsite)
		try:
			for y in range(len(data2['subdomains'])):
				y = Node(data2['subdomains'][y], parent=tsubdomains)
		except:
			pass
		try:
			tcloudflare = Node("CLOUDFLARE", parent=tsite)
			if (data['isp'] == "Cloudflare, Inc."):
				tcloudflare1 = Node(f"{Colors.OKGREEN}Cloudflare detected!{Colors.ENDC}", parent=tcloudflare)
			else:
				tcloudflare1 = Node(f"{Colors.FAIL}Cloudflare not detected!{Colors.ENDC}", parent=tcloudflare)
		except:
			pass
		try:
			trobot = Node("Robot.txt", parent=tsite)
			urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
			http = urllib3.PoolManager()
			r = http.request('GET', 'http://'+site+"/robots.txt")
			if (r.status == 200):
				trobot1 = Node(f"{Colors.OKGREEN}Robot.txt found!{Colors.ENDC}", parent=trobot)
			else:
				trobot1 = Node(f"{Colors.FAIL}Robot.txt not found!{Colors.ENDC}", parent=trobot)
		except:
			pass

		for pre, fill, node in RenderTree(tsite):
			print("%s%s" % (pre, node.name))