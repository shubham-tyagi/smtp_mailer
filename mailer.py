import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
port=465
sender_mail="raj.tyagi2000@gmail.com"
receiver_mail="sunita.tyagi1967@gmail.com"
password=input("type your password and press enter: ")

message=MIMEMultipart("alternative")
message["Subject"]="Tyagi"
message["From"]=sender_mail
message["To"]=receiver_mail

# message body is defined here
text="""\
hi,how are you ?
Shubham Tyagi is a great and humble person...
he would surely love to meet you."""
html="""\
<html>
    <body>
        <h2>Tyagi</h2>
        Check this mail out.
        <a href="www.amazon.in">great deals</a>
    </body>
</html>"""

part1=MIMEText(text,"plain")
part2=MIMEText(html,"html")
message.attach(part1)
message.attach(part2)
# attachment adding procedure
filename="document.pdf"

with open(filename,"rb") as attachment:
    part3=MIMEBase("application","octet-stream")
    part3.set_payload(attachment.read())

encoders.encode_base64(part3)
part3.add_header(
    "Content-Disposition",
    f"attachment; filename={filename}",
)
message.attach(part3)

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server :
    server.login(sender_mail,password)
    server.sendmail(sender_mail,receiver_mail,message.as_string())

print ("message sent")
