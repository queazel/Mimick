# python 2.7
#
# Hack of "test_sensor.py", which was from this page:
# https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

###----Setup----###

import RPi.GPIO as GPIO
import time
import random
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print "Waiting For Sensor To Settle"
time.sleep(2)

###----Defs----###

def measure_pulse(delay_ms):

	time.sleep(delay_ms * 0.001)
	
	# Generate 10uS pulse
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)

	# now listen
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance =round(distance,2)
	
	return distance

def send_to_pd(message=''):
	
	os.system('echo "' + str(message) + ';" | pdsend 3000')
	
###----Loop----###

for count in range(300):
	ms = random.randint(150,300) # random in case several in room
	dist = measure_pulse(ms)
	if dist < 1000: # too long
		# print "Distance: ", dist, " cm"
		send_to_pd(dist)

GPIO.cleanup()
