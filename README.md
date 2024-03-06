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

```sudo nano .bash_login```

In the file write the following : 
```cd /home/pi/BirdCapture```
```python3 main.py```

Or if you have an username :

```cd /home/<user>/BirdCapture```
```python3 main.py```


Replace <user> with the user name.

Do all required changes in ```config.cfg```,enter your lattitude and longitude
## Optional

