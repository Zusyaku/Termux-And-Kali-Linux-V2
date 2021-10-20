import dns
import dns.resolver
from prettytable import PrettyTable
from insides.Colors import Colors

def DNSLookup(site, _verbose=None):
	if _verbose != None:
		table = PrettyTable([f"{Colors.UNDERLINE}Record{Colors.ENDC}",f"{Colors.UNDERLINE}Value{Colors.ENDC}"])
		try:
			result = dns.resolver.resolve(site, 'NS')
			for ipval in result:
				table.add_row(['NS',ipval.to_text()])
		except:
			print(f"{Colors.FAIL}[NS] DNSLookup Error!{Colors.ENDC}")
		try:	
			result = dns.resolver.resolve(site, 'A')
			for ipval in result:
				table.add_row(['A',ipval.to_text()])
		except:
			print(f"{Colors.FAIL}[A] DNSLookup Error!{Colors.ENDC}")
		try:
			result = dns.resolver.resolve(site, 'MX')
			for ipval in result:
				table.add_row(['MX',ipval.to_text()])
		except:
			print(f"{Colors.FAIL}[MX] DNSLookup Error!{Colors.ENDC}")
		try:
			result = dns.resolver.resolve(site, 'TXT')
			for ipval in result:
				table.add_row(['TXT',ipval.to_text()])
			
			print("")
		except:
			print(f"{Colors.FAIL}[TXT] DNSLookup Error!{Colors.ENDC}")
		print(table)