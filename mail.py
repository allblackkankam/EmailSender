# import smtplib

# sender = 'kankamsolomon@gmail.com'
# receivers =['bgarna@gamil.com']

# message = """From:AllBlack <kankamsolomon@gmail.com> 
# 			To: Bertha <bgarna@gmail.com>
# 			Subject: SMTP e-mail test

# 			Testing Python e-mail portal"""
# try:
# 	smtp0bj =smtplib.SMTP('localhost')
# 	smtp0bj.sendmail(sender,receivers, message)
# 	print "successfully sent mail"

# except SMTPException:
# 	print "Error:unable to send email"

import smtplib

print "Email Sender"

mail = 'kankamsolomon@gmail.com'
password = 'king1234.'
message ='Testing email portal'
receivers = 'kingklan07@hotmail.com'
#gmail.server
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(mail,password)
server.sendmail( mail,receivers, message)
server.quit()

print 'Message sent'