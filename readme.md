## Live Weather Station
## Student Name: Bernard Thompson
## Student Number: 20020038

## Introduction
My aim is to develop a live weather station application which will alert devices of weather conditions and will inform a subscriber if they need to take action due to weather conditions. A raspberry pi will be used in conjunction with a Sense Hat in order to obtain temperature, humidity and air pressure. Based on these results I will also try to calculate the dew point. If time and budget allows me I would also like to acquire an anemometer to record wind speed.
Once the data above is gathered through the Sense Hat sensors, the results will be displayed live to a website which I hope to create, displaying a widget for each segment of data, while also displaying some graphs to track past records.
The pi will also be scanning the home network for connected devices (mobile phones), if the pi detects these devices on the network it will tweet the owner of the device telling them to perform an action based on the weather results, get the snow boots ready, turn the heating on, tie down the trampoline or bust out the sun cream! Something along those lines. I will also try to display a sun or a snowflake on the Sense Hat display depending if it is hot or cold.

## Tools, Technologies and Equipment. 
Hardware: Raspberry Pi, Sense Hat, anemometer (hopefully), android phone(s), Wi-Fi router.
Software: For the programming side of things I am torn between java and Python. I think I will use python as it is new to me and I may develop a better understanding of the language. I will also hope to use HTML, and CSS (possibly in the form of a bootstrap) for the website. Wia will be used to display the widgets and I am also hoping to use Blynk for mobile viewing.
In order to interact with the android devices, I will use MQTT (although this is subject to change as I will need to revisit the labs again.)

## Project Repository 
In order to store my project code, read me file and video demonstration I will use GitHub and it will be available at the following location
https://github.com/bonjo7/pi_weather_app

That about covers my scope, I hope I haven’t bitten off more than I can chew, I guess I’ll find out in a few weeks!
