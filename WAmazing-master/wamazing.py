# Ini hanya iseng-iseng gan,
# WAmazing v0.1
# 10 juni 2019 11:00pm - 11 juni 2019 1:41am
# karjok pangesty
# mengganti banner, nama author, takkan menjadikan anda seorang yang hebat :)
# 




import os,sys
import xml.etree.ElementTree as ET



os.system('clear')
print('''\033[92m
                                
                                
          ▄                  ▄      
          █▀▄              ▄▀█      
          █  ▀▄          ▄▀  █      
          █   ▀▀▀▀▀▀▀▀▀▀▀▀   █      
          █    ▄        ▄    █      
          █  ▄▀ ▀▄ ▄▄ ▄▀ ▀▄  █  █▀▀█
          █      ▄▄▄▄▄▄      █ █▀  ▄
          ▀▀▄▄▄▄▄▄▀██▀   ▄▄▄▀▀ █  ▄█
              ▀▀▀█▀▀▀▀▀▀▀▄     █  █ 
                ▄▀        ▀▄▄  █  █ 
                █  ▄   ▄    ▀▄▄█  █ 
                █  █   ██    ██  █▀ 
                █ ▄█▄ ▄█▀    █▄█▀▀  
                ▀▀▀ ▀▀▀▀▀▀▀▀▀ 
\033[93m WhatsApp Status Video Duration Increaser (\033[91mroot\033[93m)
\033[92m________________________________________________  \033[0m         
 
 
 ''')

def cekpriv():
	if os.geteuid() != 0:
		print('''[\033[91merror\033[0m] Sorry!\nIt looks like your device does not have root permission.\nThis program only runs with root access :(
If your device already has root access
but still sees this message,
Try:
	$ install tsu (pkg install tsudo)
	$ type tsu and run this program again
	$ contact https://t.me/om_karjok\033[0m''')
	else:
		up()

def up():
	q = 'com.whatsapp'
	if q in os.listdir('/data/data'):
		qq = '/data/data/com.whatsapp/shared_prefs/com.whatsapp_preferences.xml'
		os.system('cp '+qq+' '+qq+'x') # Di backup biar ga panik
		xmlfff = open(qq,'r').read() 
		xm = ET.fromstring(xmlfff)
		for table in xm.iter('map'):
			for child in table.iter('int'):
				o = child.attrib
				val = o['value']
				if 'status_video_max_duration' in o['name']:
					print(f'[\033[92m]info\033[0m] Your current status video duration is \033[92m{val} \033[0msecond')
					with open(qq,'w') as f:
						val2 = input('[\033[92minput\033[0m] Input new value (\033[93mmax:173 [2:53 min]\033[0m): ')
						if int(val2) > 173:
							val2 = '173'
							f.write(xmlfff.replace('<int name="status_video_max_duration" value="'+val+'" />','  <int name="status_video_max_duration" value="'+val2+'" />'))
							print('[\033[93mwarning\033[0m] Oops, it looks like you have entered a duration that exceeds the specified duration. But this is not a problem, because it has been justified to be 173 seconds!\nrestart your WhatsApp and try uploading a video to your WhatsApp story;)\033[0m')				
												
						else:
							f.write(xmlfff.replace('<int name="status_video_max_duration" value="'+val+'" />','  <int name="status_video_max_duration" value="'+val2+'" />'))
							print(f'[\033[92msuccess\033[0m] Great!\nNow the duration of your WhatsApp video status \nhas been set to \033[92m{val2}\033[0m seconds!\nRestart your WhatsApp and share a video \nto all of your WhatsApp contacts!\033[0m')
							
if __name__=='__main__':
	cekpriv()						
						
						
						
						
						
                                        					
