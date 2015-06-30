__author__ = 'sexybeast'

'''
* Created by sexybeast on 29 june 2015 at 10:26pm
* twitter @Mr_Ayinla
* ayinlaabdulsalam@gmail.com
'''

import requests
import json
import time
from sinchsms import SinchSMS

appKey = '213019d9-5c6d-4af6-b922-69f43aaf1c69'
secret = 'QyhpnIUJz0ulSDo6ZTXLlQ=='

client = SinchSMS(appKey, secret)


def current_weather(location):
	url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(location[0]) + '&lon=' + str(location[1])

	response = requests.get(url)

	data = json.loads(response.content)

	weather = data['weather']
	weather_description = weather[0]['description']
	main = data['main']
	temp = main['temp']
	pressure = main['pressure']
	humidity = main['humidity']
	wind = data['wind']
	wind_speed = wind['speed']
	local_time = time.asctime(time.localtime(time.time()))
	body = ". Sent from larry's farm "
	message = weather_description + ', Temperature: ' + str(temp) + ', Pressure: ' + str(
		pressure) + ', Humidity: ' + str(humidity) + ', Wind Speed: ' + str(wind_speed) + ' Time: ' + str(local_time)
	message = message + body
	return message


def send_sms(message, phone_numbers):
	for phone_number in phone_numbers:
		response = client.send_message(phone_number, message)
		print response
		#message_id = response['messageId']
		#response = client.check_status(message_id)
		#print response
		#print response['Status']


def numbers(file_loc):
	data = open(file_loc, 'r')
	phone_numbers = json.loads(data.read())
	data.close()
	return phone_numbers


farmLocation = [8.488871, 4.673192]

message = current_weather(farmLocation)
print message

phone_numbers = numbers('./numbers.json')

send_sms(message, phone_numbers)
