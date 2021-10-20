import dns, dns.resolver, urllib3
from insides.Colors import Colors

def HTTPHeaders(site,r, _verbose=None):
	if _verbose != None:

		if (r.status == 200):
			print(f"{Colors.OKGREEN}HTTP/1.1 200 OK{Colors.ENDC}")
		else:
			print(r.status)
		try:
			print(f"{Colors.WARNING}Content-Type : {Colors.ENDC}"+r.headers['Content-Type'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Server : {Colors.ENDC}"+r.headers['Server'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Set-Cookie : {Colors.ENDC}"+r.headers['Set-Cookie'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Cache-Control : {Colors.ENDC}"+r.headers['Cache-Control'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Connection : {Colors.ENDC}"+r.headers['Connection'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}X-Powered-By : {Colors.ENDC}"+r.headers['X-Powered-By'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}X-Content-Type-Options : {Colors.ENDC}"+r.headers['X-Content-Type-Options'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Access-Control-Allow-Origin : {Colors.ENDC}"+r.headers['Access-Control-Allow-Origin'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Content-Language : {Colors.ENDC}"+r.headers['Content-Language'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}X-Frame-Options : {Colors.ENDC}"+r.headers['X-Frame-Options'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}X-UA-Compatible : {Colors.ENDC}"+r.headers['X-UA-Compatible'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}X-Content-Type-Options : {Colors.ENDC}"+r.headers['X-Content-Type-Options'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}X-XSS-Protection : {Colors.ENDC}"+r.headers['X-XSS-Protection'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Access-Control-Allow-Headers : {Colors.ENDC}"+r.headers['Access-Control-Allow-Headers'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Transfer-Encoding : {Colors.ENDC}"+r.headers['Transfer-Encoding'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Content-Type : {Colors.ENDC}"+r.headers['Content-Type'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Content-Length : {Colors.ENDC}"+r.headers['Content-Length'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Content-Security-Policy : {Colors.ENDC}"+r.headers['Content-Security-Policy'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Vary : {Colors.ENDC}"+r.headers['Vary'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}Strict-Transport-Security : {Colors.ENDC}"+r.headers['Strict-Transport-Security'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}CF-Cache-Status : {Colors.ENDC}"+r.headers['CF-Cache-Status'])
		except:
			pass
		try:
			print(f"{Colors.WARNING}cf-request-id : {Colors.ENDC}"+r.headers['cf-request-id'])
		except:
			pass