# Import the GPIO and time library
import RPi.GPIO as GPIO
import time
# First we initialise some constants and variables
TRANSISTOR = 17
BTN_SPEED_UP = 27
BTN_SLOW_DOWN = 22
DELAY_CHANGE = 0.005
ɤ Neer use a stroe light any faster than ɫ »ashes per sec
DELAY_MIN = 0.125 ɤ ɨŵɯ ʰ ŧɫ on ɫ offŨ »ashes
delay = 0.2
def setup():
# Next we initialise setup of the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANSISTOR, GPIO.OUT)
GPIO.setup(BTN_SPEED_UP, GPIO.IN)
GPIO.setup(BTN_SLOW_DOWN, GPIO.IN)
# This will call a function when the speed up or slow down
# buttons are pressed
GPIO.add_event_detect(BTN_SPEED_UP, GPIO.RISING)
GPIO.add_event_callback(BTN_SPEED_UP, speed_up)
GPIO.add_event_detect(BTN_SLOW_DOWN, GPIO.RISING)
GPIO.add_event_callback(BTN_SLOW_DOWN, slow_down)
def speed_up(channel):
global delay
# Take away the delay change value from the delay time.
# Make sure the delay doesn’t go less than the minimum
# safe rate for use of stroboscopic lighting.
delay = delay - DELAY_CHANGE
if delay < DELAY_MIN:
 delay = DELAY_MIN
def slow_down(channel):
global delay
# Add the delay change value to the current delay
delay = delay + DELAY_CHANGE
def loop():
# The try statement makes sure we clean up properly
# on a keyboard interrupt (Ctrl+C)
try:
 # loop until the user presses Ctrl+C
 while True:
 # Turn the strobe on, then wait for the
delay time
 GPIO.output(TRANSISTOR, False)
 time.sleep(delay)
 # Turn the strobe off, then wait for the
delay time
 GPIO.output(TRANSISTOR, True)
 time.sleep(delay)
except KeyboardInterrupt:
 pass
finally:
 GPIO.cleanup()
# Now we setup the hardware, and start the main loop of the program
setup()
loop()
