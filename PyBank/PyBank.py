#!/bin/python
# Python Banking System ( PyBank ) ( PBS )
# By Niirmaal twaatii
# Version 1.0 [28 Jan 2019]

print("Welcome to Python Banking System 1.0 \n")
print("Author : Niirmaal Twaatii")
print("Email : twaatiiniirmall@gmail.com")
print("Youtube : https://www.youtube.com/niirmaaltwaatiitwn87 \n")
print("Instructions List:-\n 1) Deposit [deposit]\n 2) Withdraw [withdraw]\n 3) Check Amount [check]\n 4) Exit [exit] \n 5) More Instructions... [more] \n\n")

loop = 1;
amount = 1500;
subloanamount=0;
loan = 0;
loanstatus = 0;
UN = "niirmaaltwaatii"
PW = "twaatii"
adminDashStatus = 0;

while loop :
	
	inp = input("PyBank[PBS]:- ");
	
	if inp == "check" :
		print("You have Balance of Rs.%d \n" % amount)
		print("You have Rs.%d loan left \n" % loan)

        
	elif inp == "exit" :
		print("\nThanks for using the Service")
		loop = 0;
		
	elif inp == "withdraw" :
		print("\nHow much ?")
		wd = int(input("I need Rs."))
		amount -= wd
		print("\nDone ! Take your money ! Anything else ? \n");
		
	elif inp == "deposit" :
		print("\nHow much ?")
		dp = int(input("Just Rs."))
		amount += dp;
		print("\nDone! Now you have Rs.%d \n" % amount)
		if loanstatus :
			print("Also check the loan amount. Dont forget to return Loan in time !");
				
		
	elif inp == "more":
		print("\nMore Instructions:-\n 6) Loan [loan] \n 7) Admin Dashboard [dashboard] \n 8) Redeem [redeem]\n 9) Transfer Money [comming soon :)] \nAbout Creator [about] \n\n");
		
	elif inp == "loan":
		print("\nHow much ?")
		addloan = int(input("I want loan of Rs. "))
		if addloan > amount:
			loan += addloan
			print("You have total loan of Rs.%d ! Please return that in time \n" %loan)
			
		elif addloan <= amount :
			print("\nYou didn't need load ! You have enough money in your account !\n")
			
		else :
			print("loan unsucessfull !")
			
	elif inp == "dashboard" :
		print("\n\nPlease provide some information to access Admin Dashboard !\n")
		un = input("Username:- ")
		pw = input("Password:- ")
		if un == UN and pw == PW :
			adminDashStatus = 1;
			print("\nAccess Granted ! Hello %s" %UN);
			print("Type help to know your priviledges !!! \n")
		else :
			print("\nInvalid Login Details !\n")
	
	elif inp == "redeem" :
		if loanstatus :
			print("You have loan of Rs.%d !\nHow much you want to redeem ?\n" %loan)
			redeemamount = int(input("Take Rs."))
			loan -= redeemamount
			if loan > 0 :
				print("\nRs.%d loan is remaining !\n" %loan)
			elif loan==0 :
				print("\nThank you very much to return back loan ! \n")
			elif loan < 0 :
				print("\nThe excess money has been deposited !!! \n")
				loan -= amount
				print("Thank you very much to return back loan ! \n")
			else :
				print("Error Occured !!!")
			
		else :
			print("\nYou got no Loan. Enjoy !!!\n")
	
	elif inp == "calculator" :
		if adminDashStatus == 0 :
			print("Access Denied !!! \n");
		else :
			print("Calculator Opened !!")
			calculatorstatus = 1;
			while calculatorstatus :
				eq = input("Equation:- ")
				if eq == "exit" :
					calculatorstatus = 0
				else :
					eval(eq);
	elif inp == "about" :
		print("\nCreator Deatails :~")
		print("Name : Niirmaal Twaatii")
		print("Email : twaatiiniirmaal@gmail.com")
		print("Social Media : @niirmaaltwaatii")
		print("Youtube : https://www.youtube.com/niirmaaltwaatiitwn87")
		print("GitHub : https://www.github.com/niirmaaltwaatii\n")
	
	else :
		print("Sorry ! Invalid Instruction  \n");
	if loan:
		loanstatus = 1;

