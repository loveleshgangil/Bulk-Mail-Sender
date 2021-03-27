from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

send_to_mails = ["lovemrn.1668@rediffmail.com", "loveleshgangil@rocketmail.com"]
send_to_names = ["Lovelesh", "Gangil"]

for mail in send_to_mails:
    message = MIMEMultipart()
    message["from"] = "LG"
    message["to"] = mail
    message["subject"] = "Hello World"
    message.attach(MIMEText("Hello"))
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("loveleshgangil@gmail.com", "password")
        smtp.send_message(message)
        print("Sent")
