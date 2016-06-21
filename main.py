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
import requests
import json

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
# RGB Red
#myLcd.setColor(255, 0, 0)
# RGB Blue
myLcd.setColor(53, 39, 249)

# Initialize buttons using GPIO pin [2,3]
button_pb = grove.GroveButton(2)
button_touch = grove.GroveButton(3)

# Endpoint
URL = 'http://52.53.244.233:3060/v1/challenges?pretty=true'

def getValueFromTypeButton(type_button):
	messages = {
		'pb': 'a',
		'touch': 'b'
	}
	return messages.get(type_button)

def sendNotification(type_button):
	value_tb = getValueFromTypeButton(type_button)
	myLcd.clear()
	# print message
	response = requests.get(URL, None)
	data = {}
	if (response.status_code == 200):
		data = json.loads(response.text)
		if data['solution'] == value_tb:
			myLcd.write("GREAT!")
		else:
			myLcd.write("Are you sure?")
	time.sleep(1) 
	return

# Read inputs
while 1:
	if button_pb.value() == 1:
		sendNotification('pb')
	elif button_touch.value()== 1:
		sendNotification('touch')
