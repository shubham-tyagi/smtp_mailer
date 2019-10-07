import smtplib,ssl
port=465
sender_mail="raj.tyagi2000@gmail.com"
receiver_mail="sunita.tyagi1967@gmail.com"
# password="Sunita1Sudhir2"
password=input("type your password and press enter: ")
message="""\
Subject: GRE INFO 

update your gre info and updat to the office"""

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server :
    server.login(sender_mail,password)
    server.sendmail(sender_mail,receiver_mail,message)

print ("message sent")
