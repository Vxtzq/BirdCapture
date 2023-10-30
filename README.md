# BirdCapture
The simplest way to automate bird detection in your garden !

## Required Materials :
- A raspberry pi
- A battery
- An usb microphone or microphone shield
- A plastic box to fit the rpi pi and the battery (most likely waterproof)

## Setup
On raspberry pi (using raspbian) :

Don't forget to enable ssh in settings.

Clone this repository into /home/pi/ with :

```git clone https://github.com/proplayer2020/BirdCapture```

```sudo nano .bash_login```

In the file write the following : 

```python3 /home/pi/BirdCapture/main.py```

Or if you have an username :

```python3 /home/<user>/BirdCapture/main.py```

Replace <user> with the user name.

Do all required changes in ```config.cfg```,enter your lattitude and longitude, email address...
## Optional
Disable graphic interface of raspbian to reduce power usage.
