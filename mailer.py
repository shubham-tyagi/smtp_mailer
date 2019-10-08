import ssl #SSl is the standard security technology for establishing an encrypted link between gmail server and browser
import smtplib,csv
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

port=465
sender_mail="raj.tyagi2000@gmail.com" #enter mail address you want to send mail through
password=getpass.getpass("type your password and press enter: ")

#some mail account doesn't except the mail contating htmml content
#this statement is to make sure that if html part is not accepted then atleast plain part is mailed to the targeted person
message=MIMEMultipart("alternative")

message["Subject"]="Shubham Tyagi" 
message["From"]=sender_mail


# message body is defined here
text="""\
hi,how are you ?
Shubham Tyagi is a great and humble person...
he would surely love to meet you."""
html="""\
<html>
    <body>
        <h2>Tyagi</h2>
        Check this mail out.{name}
        <a href="www.amazon.in">great deals</a>
    </body>
</html>"""

#merging of html and plain part takes place here 
part1=MIMEText(text,"plain")
part2=MIMEText(html,"html")
message.attach(part1)
message.attach(part2)

# attachment adding procedure
filename="document.pdf" #you can change the file location as per your requirment
with open(filename,"rb") as attachment:
    part3=MIMEBase("application","octet-stream") #this ensures that user can download the file being sent
    part3.set_payload(attachment.read())
encoders.encode_base64(part3)
part3.add_header(
    "Content-Disposition",
    f"attachment; filename={filename}",
)
message.attach(part3) 

context=ssl.create_default_context() #validates the hostnames and its certificates and optimises the security of the connection

count=0 #this variable is defined to count the number of mails being triggered by this script

# smtpserver=input("Enter the mail server for eg: gmail or yahoo ")
# smtpserver="smtp."+str(smtpserver)+".com "
# print(type(smtpserver))

smtpserver="smtp.gmail.com"

with smtplib.SMTP_SSL(str(smtpserver),port,context=context) as server :
    server.login(sender_mail,password)
    with open("document.csv") as file:  #you can change the file location as per your requirement 
        reader=csv.reader(file)
        next(reader)                  #this line makes sure that 1st line of the csv file is skipped
        for name,email in reader:
            message["to"]=""
            message["To"]=email
            text=message.as_string()
            server.sendmail(sender_mail,email,text.format(name=name),) 
            count=count+1
            print("mail sent to "+name) #prints the name of the person to whom the mail is being sent

print ("message sent to "+str(count)+" mail addresses !!! ")
