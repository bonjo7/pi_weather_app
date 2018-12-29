
#Bernard Thompson
#Student Number 20020038
#Module Computer Networks
#Assignment IOT

#Wedsite to display weather data - http://bthompson.ie/piWeather/index.html

#Assignment description - I have set out to create a simple weather station which will display the weather data
#on a website which I have built using wia widgets. It will also use thingspeak and if the temperature falls blelow
#A value I will be tweeted informing me of the temperature and a message saying to turn on the heating

#Importing required librarys
import urllib2
import json
import time
from wia import Wia
from sense_hat import SenseHat
import time
from twython import Twython
#Assigning colour variables to display on sensehat
green = (0, 255, 0)
red = (255,0,0) 
amber = (255,191,0)
#sense python object
sense = SenseHat()
#wia python object
wia = Wia()
#Access token needed to connect device with WIA
wia.access_token = "d_sk_kNGmSQ57p1NADpytzmhZDN9t"
#Access keys and tokens required to work for twitter interaction
APP_KEY = 'omlJF10BHvUPukQyQglpry74K'
APP_SECRET = 'k42Vu7OFsefCfBwons7TekafL0qTfTAjWiP8U6FsMt8tzrNkXv'
OAUTH_TOKEN = '1079070521948540928-DGExLZrQpQVGjg6hVmNeRuSZKhABaX'
OAUTH_TOKEN_SECRET = 'xOJYVZWhX04QobhaaopozUMGToNH0jNSyFijMtChfD3PG'
#twitter python object
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Running a while loop
#While true gather the data from the sense hat every 60 seconds
#This can then graph the weather data while ensuring
#The most recent data is available
while True:
	#Get the temperature from the sensehat
	#I had to calibarate this to try and get an accurate reading
	#After various tests comparing online weather sites and termostats
	#I found subtracting 13 to be the closet to accurate
	temp = round(sense.get_temperature(), 0) - 13
	wia.Event.publish(name="temperature", data=temp)

	#Using the temperature to calculate the fahrenheit vaule
	tempFahrenheit = 1.8 * temp + 11 
	wia.Event.publish(name="fahrenheit", data=tempFahrenheit)

	#Get the humidity value from the sensehat
	humidity = round(sense.get_humidity() , 0)
	wia.Event.publish(name="humidity", data=humidity) 

	#Get the pressure from the sensehat
	pressure = round(sense.get_pressure(), 0)
	wia.Event.publish(name="pressure", data=pressure)

	#Using the humidity and temperature I calculated the dew point
	#This was trial and error to get it accurate.
	#I found a formual online but the readings were way off
	#I used online weather sites and adjusted the formula to get a close to accurate as possible
	#I could not measure relative humidty as that required a sensor so I based it off the sensehat humidity sensor
	dewPoint = round(((((humidity / 100) * 0.125) * ((112 + 0.9) * temp ) + (0.1 * temp))) - 85 , 0)
	wia.Event.publish(name="dewpoint", data=dewPoint)

	#Creating a connection with thingspeak in order to tweet myself if the temperature drops below 10c
	#If the value falls below 10c I will be informed and told to turn on the heating
	#Using try method so if it fails I will have been warned about the failure
	#To turn on the heating Blynk is used as a simple button which will
	#Illuminate the sensehat leds to green for on
	#def writedate(temp):
	try:
		conn = urllib2.urlopen('https://api.thingspeak.com/update?api_key=ZYH76UKXGEM8YYMX' + '&field1=%s&field2=%s' % (temp, dewPoint))
		#Close the connection to thingspeak
		conn.close()

	except Exception as e:
		print(str(e))	

	#Tried to crate this as a function but it wouldn't work so commented out some code
	#Here I am simulating the sensehat as a screen in the house
	#If the dew point in between values as below it will display in the sensehat
	#Telling those in the house what the conditions are as the dewpoint
	#Represents the water vapour present in the air
	#def dewPointCheck(dewPoint):

	#Clearing sensehat if anyting is present on LED's
	sense.clear()

	if (dewPoint >= -10) or (dewPoint <= 10):
		sense.show_message("Uncomfortable", text_colour = green)
	elif (dewPoint >= 11) or (dewPoint <= 25):
		sense.show_message("Comfortable", text_colour = red)
	elif (dewPoint >= 26) or (dewPoint <= 40):
		sense.show_message("Not so comfortable", text_colour = amber)
	#	return		
	
	#Get current system date and time from the pi
	datetime = time.strftime('%m/%d/%Y %H:%M:%S')
	#Create variable for twitter post to display the date and time and weather data
	twitterMsg = 'Current weather status for ' + datetime + ' : Temperature ' + str(temp) + 'c, DewPoint ' + str(dewPoint) + 'c, Humidity ' + str(humidity) + '%'
	#Post tweet to twitter
	#Using try method so if it fails I will have been warned about the failure
	try:
		twitter.update_status(status=twitterMsg )
	except Exception as e:
		print(str(e))
	#Set the sleep to every 30 minutes and loop through the above
	time.sleep(1800)







	
		


	