# python 2.7
#
# Testing ultrasonic sensor following instruction on this page:
# https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print "Waiting For Sensor To Settle"

time.sleep(2)

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

print "Distance: ", distance, " cm"

GPIO.cleanup()
