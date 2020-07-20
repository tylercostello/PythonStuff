exec("""
import urllib2
import RPi.GPIO as GPIO
import time

url = "https://tyco333.000webhostapp.com/relay-status.txt"

GPIO.setup(Pin17, GPIO.OUT)

while 1:
	relaystatus = urllib2.urlopen(url).read(1)
	if relaystatus=="1":
		 GPIO.output(17, GPIO.LOW)
	elif relaystatus == "0":
		 GPIO.output(17, GPIO.HIGH)
	time.sleep(2)
""")