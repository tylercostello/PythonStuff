import smtplib
import time
def sendemail(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("emailuser", "emailpass")
	server.sendmail("emailuser", "emaildest", msg)
	server.quit()
sendemail("a test")