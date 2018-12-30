### Name: Bernard Thompson
### Student Number: 20020038
### Module: Computer Networks
### Assignment: Assignment 2, iot Project.
### Project Name: Pi Weather Station
### Git Repo: [Git Repo](https://github.com/bonjo7/pi_weather_app)
### Youtube video: [Video](https://www.youtube.com/watch?v=-ApTRzOWjRs)

## Introduction
For this project I used the raspberry pi with a sense hat. The on-board sensors were used to gather the
Temperature, humidity and air pressure. As well I this I performed calculations in order to obtain the
Dew point and Fahrenheit.

## Project
The weather data was sent and stored with [WIA](https://www.wia.io/) where I created widgets. These widgets
are displayed on a website [PiWeatherWebSite](http://bthompson.ie/piWeather/index.html) which is a free bootstrap template. This required
some changes to display the widgets correctly and changing, the background, title are and adding a social section "twitter".

Using twitter developer options, I was able to create a small twitter app which allows the twitter account @PiWeather1 to tweet
the weather conditions every half hour which can be seen here [@PiWeather1](https://twitter.com/PiWeather1?lang=en)

The next step was to use [ThingSepak](https://thingspeak.com/) in order to create two "reacts", one to check temperature and the other
to check the dew point. If either value fell below 10c the @PiWeather1 would tweet my personal twitter account @bonjo7 informing
me of the drop and tell to either turn on the heating or take action.

Once I received this tweet, I could then use the [blynk](https://www.blynk.cc/) to simulate turning on the heating. Pressing
a button via the app, would illuminate the sense hat in green, meaning the heating was turned on.

The script also scans the network to detect if either of two devices are connected. If it detects the device a message relating
to the dew point is displayed on the sense hat (simulating a screen in the house), the user would then know of you put on lip balm
before going outside due to dry conditions.

## Resources
It was mainly all the labs as I felt if I followed projects available online, I would just have been coping and replicating, therefore
I opted to follow the labs as I felt I could best learn that way. I used python as I had not previously used python so it was a nice learning
curve.

For the integration with twitter I visited the twitter developer [site](https://developer.twitter.com/content/developer-twitter/en.html) and browsed
the documentation and resources.

To calculate the dew point I used the following formula https://www.ajdesigner.com/phphumidity/dewpoint_equation_dewpoint_temperature.php#ajscroll

I had an issue when connected via ssh, the scripts would run but once I disconnected the scripts would then stop. I found the following commands via 
a tutorial which allowed me to run the scripts in screens, so when I disconnect via ssh they would still run.
This also allows me to run both a python script and a nodejs file together.

#### Install screen
sudo apt-get install screen
#### Run Script
screen python wiaSenseHat.py & </br>
screen node index.js &
#### List Screens
screen -list
#### Enter a screen and stop script if required
screen -r <screen id>
  
## Run the scripts
In order to run the node js script first ensure node is installed first. 
The type the following commands

#### Check if Node is already on the pi. If so,you are adviced to remove it and reinstall as follows:
sudo apt-get purge node nodejs node.js -y
sudo apt-get autoremove

#### Update package repository and install node:
curl -sL "https://deb.nodesource.com/setup_6.x" | sudo -E bash -
sudo apt-get install build-essential nodejs -y
sudo apt-get install npm

#### Naviagte to the folder location where the project is saved
npm init
sudo npm install blynk-library --save
sudo npm install onoff ---save

#### Install snese hat
npm install node-sense-hat --save

## Run the python script
TO ensure the Arp scan works we need to install arp-scan onto your device, enter the following commands
sudo apt-get update
sudo apt-get install arp-scan

#### Next we need to install WIA
pip install wia  
