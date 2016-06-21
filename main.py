#!/usr/bin/env python

#######################
#
# OLEO Project
#
# @description: platform to development congnitive process on childrens.
# #author: OLEO-Team
#
#######################

import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
# RGB Red
#myLcd.setColor(255, 0, 0)
# RGB Blue
myLcd.setColor(53, 39, 249)

# Initialize buttons using GPIO pin [2,3]
button_pb = grove.GroveButton(2)
button_touch = grove.GroveButton(3)

def getMessage(type_button):
	messages = {
		'pb': 'Push button',
		'touch': 'Touch'
	}
	return messages.get(type_button)

def sendNotification(type_button):
	message = getMessage(type_button)
	myLcd.setCursor(0,0)
	myLcd.write(message)
	time.sleep(1) 
	return

# Read inputs
while 1:
	if button_pb.value() == 1:
		sendNotification('pb')
	elif button_touch.value()== 1:
		sendNotification('touch')
