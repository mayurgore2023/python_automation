# application for sending mail with attachment:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Storing sender and receiver email address
sender_mail = "sender@gmail.com"     # sender mail address
receiver_mail = "receiver@gmail.com" # receiver mail address

# creating instance of MIMEMultipart
message = MIMEMultipart()

# Assigning sender_email,receiver_email & sub of mail
message["From"] = 'sender@gmai.com '             # sender_mail
message["To"] =   "reciver@gmail.com"            #receiver_mail
message["Subject"] = "Sending mail using python"

# Attach body of mail
body = "Hello,\n This message from Python "
message.attach(MIMEText(body,'plain'))


# As we have to mail the file "doc.txt" it's open in read-only in binary format mode
File = "File name"           # give file name or file path  for sending as a attachment
Attachment = open(File,'rb')

# Creating instance of MIMEBase
Obj =  MIMEBase('application','octet-stream')

# Payload is the file that we are mailing  & here payload is encoded
Obj.set_payload((Attachment).read())
encoders.encode_base64(Obj)
Obj.add_header('Content-Disposition',"Attachment; filename="+File)

# Attaching obj to our massage:
message.attach(Obj)

# converting message into string
my_message = message.as_string()

# using server send mail
Server = smtplib.SMTP('smtp.gmail.com',587)
Server.starttls()
Server.login(sender_mail,'password')   # write app mail password

Server.sendmail(sender_mail,receiver_mail,my_message)

Server.quit()







