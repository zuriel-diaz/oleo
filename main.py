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

# Initialize buttons using GPIO pin [2,3]
button_pb = grove.GroveButton(2)
button_touch = grove.GroveButton(3)

def sendNotification(type_button):
	print "test", 
	return

# Read inputs
while 1:
	if button_pb.value() == 1:
		sendNotification('pb')
	elif button_touch.value()== 1:
		sendNotification('touch')
