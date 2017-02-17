# Importing all necessary libraries
import pico
import os
import sys
import json
import time
from os import getenv
import pymssql

def SMARTResp(query):
	import apiai
	ai = apiai.ApiAI('7fea9fc7dda34c83b6e08057bc710bf9')
	request = ai.text_request()
	time.sleep(2)
	request.query = query
	
	response = json.loads(request.getresponse().read())
	time.sleep(2)

	final_resp = response['result']['fulfillment']['speech']
	
	time.sleep(2)
	return final_resp
##
##a = SMARTResp('Hi')
##print a
