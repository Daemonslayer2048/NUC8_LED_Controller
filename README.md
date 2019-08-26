# NUC8_LED_Controller
A project to help control Intels NUC8 LEDs

## How it works
LED_Controller.py uses psutil to get basic system info (Mainly CPU percent used, CPU package temp, and RAM used).  
From there some basic math is used to shift the LEDs from Blue to Red. This is a simple proof of concept right now.  
* The Eyes of the skull are based on package temp.  
* The skull is based on CPU used.  
* The 1st LED is based on hard drive usage (only defined in this script but not controlled by this script).  
* The 2nd LED is based on ethernet usage (only defined in this script but not controlled by this script).  
* The 3rd LED is based on RAM used.
* The power button is also set to indicate power limit

## To install
If you would like to use this script as a service you will need to place ```NUC8_LED_Controller.service``` into ```/etc/system/systemd/```. After you complete that add the working directory and path to script where indicated. Finally run the following:  
```
sudo systemctl start NUC8_LED_Controller
```
And to make it start on boot:
```
sudo systemctl enable NUC8_LED_Controller
```


### Prerequisites
https://github.com/nomego/intel_nuc_led

Most imports used should come with your system by default if not they are listed below:
* time
* psutil
* logging
* systemd
