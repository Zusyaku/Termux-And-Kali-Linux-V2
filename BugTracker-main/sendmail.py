import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import app

# Sending confirmation email to the reporter


class ReporterSendMail:
    def __init__(self, recipient_email, system, severity, steps, message):
        # Email and password for your SMTP server
        email = app.config['SMTP_EMAIL']
        password = app.config['SMTP_PASSWORD']
        subject = 'Thanks for reporting the bug'
        # The email needs to be written in HTML first then pure text for complete compatibility
        messageHTML = f'<table style="height: 40px; border-color: black; margin-left: auto; margin-right: auto;" width="1109"><tbody><tr><td style="width: 1099px; text-align: center;"><h1>Thanks for reporting the bug</h1></td></tr></tbody></table><h2>&nbsp;</h2><h2>Summary of your report:</h2><table style="height: 196px; width: 927px; border-color: black; margin-left: auto; margin-right: auto;"><tbody><tr style="height: 30px;"><td style="height: 30px;"><div><h3>System</h3></div></td><td style="width: 212.133px; height: 30px;"><h3>&nbsp;{system}</h3></td></tr><tr style="height: 27px;"><td style="width: 226.867px; height: 27px;"><div><h3>Severity</h3></div></td><td style="width: 212.133px; height: 27px;"><h3>&nbsp;{severity}</h3></td></tr><tr style="height: 122.433px;"><td style="width: 226.867px; height: 122.433px;"><div><h3>Steps to reproduce</h3></div></td><td style="width: 212.133px; height: 122.433px;"><h3>&nbsp;{steps}</h3></td></tr><tr style="height: 98px;"><td style="width: 226.867px; height: 98px;"><h3>Message</h3></td><td style="width: 212.133px; height: 98px;"><h3>&nbsp;{message}</h3></td></tr></tbody></table><p>&nbsp;</p>'
        messagePlain = f"Thanks for reporting the bug\nSummary of your report:\nSystem {system}\nSeverity {severity}\nSteps to reproduce {steps}\nMessage {message}\nPlease enable HTML to see the styled message."
        # We define the MIME module and say that there is an alternative for the HTML email for it to use it
        msg = MIMEMultipart('alternative')
        # Defining email, recipient email and subject for the MIME module
        msg['From'] = email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        # Then we attach our message both in plain text and html
        msg.attach(MIMEText(messagePlain, 'plain'))
        msg.attach(MIMEText(messageHTML, 'html'))
        # We define our SMTP server (using gmail here you need to enable less secure apps to use it)
        server = smtplib.SMTP(app.config['SMTP_HOST'], app.config['SMTP_PORT'])
        # Starting a secure TLS connection and logining in
        server.starttls()
        server.login(email, password)
        # turning the MIME message into string and finally sending the email then closing the connection
        text = msg.as_string()
        server.sendmail(email, recipient_email, text)
        server.quit()


class AdminSendMail:
    def __init__(self, recipient_email, system, severity, steps, message):
        # Email and password for your SMTP server
        email = app.config['SMTP_EMAIL']
        password = app.config['SMTP_PASSWORD']
        subject = 'A new bug has been reported'
        # The email needs to be written in HTML first then pure text for complete compatibility
        messageHTML = f'<table style="height: 40px; border-color: black; margin-left: auto; margin-right: auto;" width="1109"><tbody><tr><td style="width: 1099px; text-align: center;"><h1>Thanks for reporting the bug</h1></td></tr></tbody></table><h2>&nbsp;</h2><h2>Summary of the report:</h2><table style="height: 196px; width: 927px; border-color: black; margin-left: auto; margin-right: auto;"><tbody><tr style="height: 30px;"><td style="height: 30px;"><div><h3>System</h3></div></td><td style="width: 212.133px; height: 30px;"><h3>&nbsp;{system}</h3></td></tr><tr style="height: 27px;"><td style="width: 226.867px; height: 27px;"><div><h3>Severity</h3></div></td><td style="width: 212.133px; height: 27px;"><h3>&nbsp;{severity}</h3></td></tr><tr style="height: 122.433px;"><td style="width: 226.867px; height: 122.433px;"><div><h3>Steps to reproduce</h3></div></td><td style="width: 212.133px; height: 122.433px;"><h3>&nbsp;{steps}</h3></td></tr><tr style="height: 98px;"><td style="width: 226.867px; height: 98px;"><h3>Message</h3></td><td style="width: 212.133px; height: 98px;"><h3>&nbsp;{message}</h3></td></tr></tbody></table><p>&nbsp;</p>'
        messagePlain = f"Thanks for reporting the bug\nSummary of your report:\nSystem {system}\nSeverity {severity}\nSteps to reproduce {steps}\nMessage {message}\nPlease enable HTML to see the styled message."
        # We define the MIME module and say that there is an alternative for the HTML email for it to use it
        msg = MIMEMultipart('alternative')
        # Defining email, recipient email and subject for the MIME module
        msg['From'] = email
        msg['To'] = app.config['ADMIN_EMAIL']
        msg['Subject'] = subject
        # Then we attach our message both in plain text and html
        msg.attach(MIMEText(messagePlain, 'plain'))
        msg.attach(MIMEText(messageHTML, 'html'))
        # We define our SMTP server (using gmail here you need to enable less secure apps to use it)
        server = smtplib.SMTP(app.config['SMTP_HOST'], app.config['SMTP_PORT'])
        # Starting a secure TLS connection and logining in
        server.starttls()
        server.login(email, password)
        # turning the MIME message into string and finally sending the email then closing the connection
        text = msg.as_string()
        server.sendmail(email, app.config['ADMIN_EMAIL'], text)
        server.quit()
