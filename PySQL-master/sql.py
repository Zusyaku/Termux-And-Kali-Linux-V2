#!/dimana saja
# coding=utf-8
"""
- PySQL
# Usage = python3
# Asthor = Karjoq-Kun With Dobleh-Kun
# Source : https://github.com/rezadkim
"""
# WARNA #
t = "\033[1;97m"
m = "\033[1;91m"
u = "\033[1;95m"
h = "\033[1;92m"
k = "\033[1;93m"
b = "\033[1;96m"
logo = t+"""
╔═╗"""+m+"""┬ ┬"""+t+"""╔═╗╔═╗ ╦
╠═╝"""+m+"""└┬┘"""+t+"""╚═╗║═╬╗║
╩   """+m+"""┴ """+t+"""╚═╝╚═╝╚╩═╝\nCreator > """+h+"""Rezadkim\n"""+t+"""Source > """+h+"""https://github.com/rezadkim"""

import os,sys,time
import json
import mysql.connector

def tyk():
	os.system("clear")
	print(logo)
	print(k+36*"-")
	q = input(t+"["+h+"?"+t+"] are you already running localhost [y/n]: "+h)
	if q =="y":
		login()
	else:
		exit(t+"["+m+"!"+t+"] Exit")	

def login():
	global hot,us,ps
	try:
		os.system("clear")
		print(logo)
		print(k+36*"-")
		hot = input(t+"["+b+"+"+t+"] Host ("+b+"localhost"+t+") : "+h)
		us = input(t+"["+b+"+"+t+"] Username : "+h)
		ps = input(t+"["+b+"+"+t+"] Password : "+h)
		print(t+"["+h+"%"+t+"] Menghubungkan ke Database ...")
		time.sleep(2)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps)
		if db.is_connected():
			print(t+"["+h+"*"+t+"] Berhasil terhubung ke database")
			p = ("{'host':'"+hot+"', 'username':'"+us+"', 'password':'"+ps+"'}")
			s = open("config.json","w")
			s.write(p)
			s.close()
			input("["+b+"Enter"+t+"] Untuk melanjutkan ...")
			main()
	except:
		print(t+"["+m+"!"+t+"] Error")

def main():
	os.system("clear")
	print(logo)
	print(k+36*"-")
	print(t+"["+b+"*"+t+"] Host "+m+": "+h+hot)
	print(t+"["+b+"*"+t+"] User "+m+": "+h+us)
	print(k+10*"-")
	print(t+"["+h+"1"+t+"] Create Database")
	print(t+"["+h+"2"+t+"] Create Table")
	print(t+"["+h+"3"+t+"] Insert Data")
	print(t+"["+h+"4"+t+"] Show all data from the table")
	print(t+"["+h+"5"+t+"] Edit data")
	print(t+"["+h+"6"+t+"] Delete data")
	print(t+"["+h+"7"+t+"] Search data")
	print(t+"["+h+"8"+t+"]"+m+" Exit")
	p = input(t+"\n["+b+">>"+t+"] Choose : "+h)
	if p =="1":
		create_db()
	elif p =="2":
		create_tb()
	elif p =="3":
		insert_dt()
	elif p =="4":
		show_tb()
	elif p =="5":
		edit()
	elif p =="6":
		delete()
	elif p =="7":
		search()
	elif p =="8":
		print(t+"["+m+"!"+t+"] Exit")
		exit()
	else:
		exit(t+"["+m+"!"+t+"] Exit")

#---------------------------------------------------------------------------------------------------#
def create_db():
	try:
		db = mysql.connector.connect(host=hot,user=us,passwd=ps)
		name = input(t+"\n["+b+"+"+t+"] Name Database : "+h)
		print(t+"["+h+"%"+t+"] Membuat Database baru ...")
		time.sleep(2)
		cursor = db.cursor()
		cursor.execute("CREATE DATABASE "+name)
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()
	print(t+"["+h+"*"+t+"] Database berhasil dibuat : "+u+name)
	input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
	main()

def create_tb():
	try:
		debe = input(t+"\n["+h+"+"+t+"] Input name database : "+h)
		name_tb = input(t+"["+h+"+"+t+"] Create name table : "+h)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps,database=debe)
		cursor = db.cursor()
		sql = "CREATE TABLE "+name_tb+" (user_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address Varchar(255),username Varchar(255),password Varchar(255))"
		print(t+"["+h+"%"+t+"] Membuat tabel baru ...")
		time.sleep(2)
		cursor.execute(sql)
		print(t+"["+h+"*"+t+"] Tabel berhasil dibuat : "+u+name_tb)
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()

def insert_dt():
	try:
		debe = input(t+"\n["+h+"+"+t+"] Input name database : "+h)
		name_tb = input(t+"["+h+"+"+t+"] Input name table : "+h)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps,database=debe)
		print(t+"["+h+"?"+t+"] Enter data below to create data table contents")
		nama = input(t+"Name : "+h)
		address = input(t+"Address : "+h)
		username = input(t+"Username : "+h)
		password = input(t+"Password : "+h)
		val = (nama, address, username, password)
		cursor = db.cursor()
		sql = "INSERT INTO "+name_tb+" (name, address, username, password) VALUES (%s, %s, %s, %s)"
		print(t+"["+h+"%"+t+"] Memasukkan data baru ...")
		time.sleep(2)
		cursor.execute(sql, val)
		db.commit()
		print(t+"["+h+"*"+t+"] data telah ditambahkan")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()

def show_tb():
	try:
		debe = input(t+"\n["+h+"+"+t+"] Input name database : "+h)
		tb = input(t+"["+h+"+"+t+"] Input name table : "+h)
		print(t+"["+h+"%"+t+"] Dump all data ...")
		time.sleep(2)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps,database=debe)
		cursor = db.cursor()
		sql = ("SELECT * FROM "+tb)
		cursor.execute(sql)
		hasil = cursor.fetchall()
		if cursor.rowcount < 0:
			print(t+"["+k+"!"+t+"] Data kosong")
			input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
			main()
		else:
			print(k+40*"-"+h)
			for isi in hasil:
				print(isi)
				print(k+40*"-"+h)
			input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
			main()
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()

def edit():
	try:
		debe = input(t+"\n["+h+"+"+t+"] Input name database : "+h)
		tb = input(t+"["+h+"+"+t+"] Input name table : "+h)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps,database=debe)
		cursor = db.cursor()
		sql = ("SELECT * FROM "+tb)
		cursor.execute(sql)
		hasil = cursor.fetchall()
		if cursor.rowcount < 0:
			print(t+"["+k+"!"+t+"] Data kosong")
			input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
			main()
		else:
			print(k+40*"-"+h)
			for isi in hasil:
				print(isi)
				print(k+40*"-"+h)
		user_id = input(t+"["+h+"+"+t+"] Choose id user : "+h)
		print(t+"["+h+"?"+t+"] Update data contents")
		nama = input(t+"New Name : "+h)
		address = input(t+"New Address : "+h)
		username = input(t+"New Username : "+h)
		password = input(t+"New Password : "+h)
		sql = "UPDATE "+tb+" SET name=%s, address=%s, username=%s, password=%s WHERE user_id=%s"
		val = (nama, address, username, password, user_id)
		cursor.execute(sql, val)
		db.commit()
		print(t+"["+h+"*"+t+"] data telah diperbarui")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()

def delete():
	try:
		debe = input(t+"\n["+h+"+"+t+"] Input name database : "+h)
		tb = input(t+"["+h+"+"+t+"] Input name table : "+h)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps,database=debe)
		cursor = db.cursor()
		sql = ("SELECT * FROM "+tb)
		cursor.execute(sql)
		hasil = cursor.fetchall()
		if cursor.rowcount < 0:
			print(t+"["+k+"!"+t+"] Data kosong")
			input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
			main()
		else:
			print(k+40*"-"+h)
			for isi in hasil:
				print(isi)
				print(k+40*"-"+h)
		user_id = input(t+"["+h+"+"+t+"] Choose id user : "+h)
		sql = "DELETE FROM "+tb+" WHERE user_id=%s"
		val = (user_id,)
		cursor.execute(sql, val)
		db.commit()
		print(t+"["+h+"*"+t+"] data telah dihapus")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()

def search():
	try:
		debe = input(t+"\n["+h+"+"+t+"] Input name database : "+h)
		tb = input(t+"["+h+"+"+t+"] Input name table : "+h)
		db = mysql.connector.connect(host=hot,user=us,passwd=ps,database=debe)
		cursor = db.cursor()
		key = input(t+"["+h+"+"+t+"] Query : "+h)
		sql = "SELECT * FROM "+tb+" WHERE name LIKE %s OR address LIKE %s"
		val = ("%{}%".format(key), "%{}%".format(key))
		cursor.execute(sql, val)
		hasil = cursor.fetchall()
		if cursor.rowcount < 0:
			print(t+"["+k+"!"+t+"] Data kosong")
			input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
			main()
		else:
			print(k+40*"-"+h)
			for isi in hasil:
				print(isi)
				print(k+40*"-"+h)
			input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
			main()
	except:
		print(t+"["+m+"!"+t+"] Error")
		input(t+"["+b+"Enter"+t+"] Untuk kembali ke menu ...")
		main()

tyk()