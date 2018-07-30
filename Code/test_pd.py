# python 2.7
#
# Hack of code from this page:
# https://guitarextended.wordpress.com/2012/11/03/make-python-and-pure-data-communicate-on-the-raspberry-pi/

###----Setup----###

import time
import os

print "starting PD test"
time.sleep(2)

def send_to_pd(message=''):
	os.system('echo ' + message + ' | pdsend 3000')
	
	


for count in range(300):
	ms = random.randint(50,100) # random in case several in room
	dist = measure_pulse(ms)
	if dist < 1000: # too long
		print "Distance: ", dist, " cm"

GPIO.cleanup()
