# BirdCapture
The simplest way to automate bird detection in your garden !

## Required Materials :
- A raspberry pi
- A battery
- An usb microphone or microphone shield
- A plastic box to fit the rpi pi and the battery (most likely waterproof)

## Setup
On raspberry pi (using raspbian) with working python environement (use raspbian legacy version):
### Raspberry pi config

###Don't use an username as it will mess up some features, keep "pi" username###

Enable ssh by going into start menu > Preferences > Raspberry Pi Configuration click on Interfaces and click enable next to SSH and click OK 

Enter ```raspi-config``` in command prompt

Disable graphic interface of raspbian by ssh to reduce power usage, its easy to find either in command line using raspi-config or in raspberry pi settings.
### Enable wifi access point
You will need to eable wifi access point from your raspberry pi to access birdcapture from your phone for example.
Follow this tutorial : 
https://www.tomshardware.com/how-to/raspberry-pi-access-point
### Repository setup

Clone this repository into /home/pi/ with :

```git clone https://github.com/proplayer2020/BirdCapture```

Then, just execute the script main.py once in a python editor on the raspberry pi : the program will move the required files to auto start next times

Do all required changes in ```config.cfg```,enter your lattitude and longitude
## Optional
