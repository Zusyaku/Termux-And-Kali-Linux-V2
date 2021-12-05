import os
import sys
import urllib2
import time

R = '\033[1;34m'
G = '\033[1;31m'
B = '\033[1;92m'
A = '\033[1;80m'
cyan = '\033[1;36m'
lolcat = '\033[1;33m'
about = """
############################################
###                                        #
# Name: Admin finder python2 script.       #
# Author: AnonyminHack5                    #
# Github: https://github.com/TermuxHackz/  # 
# Usage: python2 admin.py                  #
# Note: Let website have <http> not <https>#
############################################
""" 

print ""
goodbye = "Good bye, Remember be a white hat, AnonyminHack5 loves you all. And thanks for using my script."
banner =  """\033[1;32m
              _           _         ______ _           _           
     __      | |         |_|       |  ____|_|         | |          
    /  \   __| |_ __ ___  _ _ __   | |__   _ _ __   __| | ___ _ __ 
   / /\ \ / _` | '_ ` _ \| | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
  / ____ \ (_| | | | | | | | | | | | |    | | | | | (_| |  __/ |   
 /_/    \_\__,_|_| |_| |_|_|_| |_| |_|    |_|_| |_|\__,_|\___|_|
 ++++++++++++++++++++++++++++v1.0++++++++++++++++++++++++++++++++
++Created by: AnonyminHack5 ++
++Tool: Admin Panel Finder ++
++Team: Termux Android Hackers ++
++Note: Use http ++
\033[1;96m
"""
os.system("cls || clear")
print ""
print(about+ lolcat)
print(R+ "---//--Please wait for 5 secs before the tool sets up---//--") 
time.sleep(5)
print ""
os.system("cls || clear") 
print(G+ "Now the tool will setup now.. Stand by.. ") 
print(cyan+ about) 
print ""
print(A+ "This tool gets the admin login pages of sites") 
time.sleep(3)
os.system("cls || clear") 
print banner
site = raw_input(cyan+ "[*]Please type url of Website[*]: ") 
if "http://" not in site:
    site ="http://"+site
admin = ['/admin/','/administrator/','/admin1/','/cms/','/admin2/','/admin3/','/admin4/','/admin5/','/usuarios/','/usuario/','/administrator/','/moderator/','/webadmin/','/adminarea/','/bb-admin/','/adminLogin/','/admin_area/','/panel-administracion/','/instadmin/',
'/memberadmin/','/administratorlogin/','/adm/','/admin/account.php','/admin/index.php','/admin/login.php','/admin/admin.php','/admin/account.php',
'/admin_area/admin.php','/admin_area/login.php','/siteadmin/login.php','/siteadmin/index.php','/siteadmin/login.html','/admin/account.html','/admin/index.html','/admin/login.html','/admin/admin.html',
'/admin_area/index.php','/bb-admin/index.php','/bb-admin/login.php','/bb-admin/admin.php','/admin/home.php','/admin_area/login.html','/admin_area/index.html',
'/admin/controlpanel.php','/admin.php','/admincp/index.asp','/admincp/login.asp','/admincp/index.html','/admin/account.html','/adminpanel.html','/webadmin.html',
'/webadmin/index.html','/webadmin/admin.html','/webadmin/login.html','/admin/admin_login.html','/admin_login.html','/panel-administracion/login.html',
'/admin/cp.php','/cp.php','/administrator/index.php','/administrator/login.php','/nsw/admin/login.php','/webadmin/login.php','/admin/admin_login.php','/admin_login.php',
'/administrator/account.php','/administrator.php','/admin_area/admin.html','/pages/admin/admin-login.php','/admin/admin-login.php','/admin-login.php',
'/bb-admin/index.html','/bb-admin/login.html','/acceso.php','/bb-admin/admin.html','/admin/home.html','login.php','/modelsearch/login.php','/moderator.php','/moderator/login.php',
'/moderator/admin.php','/account.php','/pages/admin/admin-login.html','/admin/admin-login.html','/admin-login.html','/controlpanel.php','/admincontrol.php',
'/admin/adminLogin.html','/adminLogin.html','/admin/adminLogin.html','/home.html','/rcjakar/admin/login.php','/adminarea/index.html','/adminarea/admin.html',
'/webadmin.php','/webadmin/index.php','/webadmin/admin.php','/admin/controlpanel.html','/admin.html','/admin/cp.html','/cp.html','/adminpanel.php','/moderator.html',
'/administrator/index.html','/administrator/login.html','/user.html','/administrator/account.html','/administrator.html','/login.html','/modelsearch/login.html',
'/moderator/login.html','/adminarea/login.html','/panel-administracion/index.html','/panel-administracion/admin.html','/modelsearch/index.html','/modelsearch/admin.html',
'/admincontrol/login.html','/adm/index.html','/adm.html','/moderator/admin.html','/user.php','/account.html','/controlpanel.html','/admincontrol.html',
'/panel-administracion/login.php','/wp-login.php','/adminLogin.php','/admin/adminLogin.php','/home.php','/admin.php','/adminarea/index.php',
'/adminarea/admin.php','/adminarea/login.php','/panel-administracion/index.php','/panel-administracion/admin.php','/modelsearch/index.php',
'/modelsearch/admin.php','/admincontrol/login.php','/adm/admloginuser.php','/admloginuser.php','/admin2.php','/admin2/login.php','/admin2/index.php','/usuarios/login.php',
'/adm/index.php','/adm.php','/affiliate.php','/adm_auth.php','/memberadmin.php','/administratorlogin.php','/user/login','administrator','log','log.php']
for i in admin:
    try:
        adminpanel = urllib2.urlopen(site+i)
        checkurl = adminpanel.code
        if checkurl ==200:
            print site+i,''' [!] Enter [!]'''
            continue
    except urllib2.URLError, checkurl:
        if checkurl == 404:
            print site+i," ""    Not Found :/"
        else:
            print site+i,''' Error 404 '''
print ""
print(B+ goodbye) 
	
            
            
            
            
