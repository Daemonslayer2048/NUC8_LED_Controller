#! /usr/bin/python3
#################################################################
# Imports
import time
import psutil
import logging
from systemd import journal

#################################################################
# Globals
acpi = "/proc/acpi/nuc_led"
zones = {
    "power": "0",
    "skull": "2",
    "eyes": "3",
    "left_led": "4",
    "center_led": "5",
    "right_led": "6"
}
cpu_temp_low = 40
cpu_temp_high = 80
#################################################################
# Functions
def startup_leds():
    # I want to make this next part readable so users know what is being set here
    configs = []
    #Set Power LED to indicate Power Limit
    configs.append("set_indicator,0,5")
    #Set Skull to software
    configs.append("set_indicator,2,0")
    #Set Eyes to software
    configs.append("set_indicator,3,0")
    #Set 1st LED to HDD
    configs.append("set_indicator,4,1")
    #Set 2nd LED to Ethernet
    configs.append("set_indicator,5,2")
    #Set 3rd LED to software
    configs.append("set_indicator,6,0")
    # Set them now
    with open(acpi, "w") as setup:
        for config in configs:
            with open(acpi, "w") as led:
                led.write(config)
                journal.send(str(config))

def set_color(zone, Red, Green, Blue):
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,1," + str(Red) + "\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,2," + str(Green) + "\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,3," + str(Blue) + "\n")

def set_eyes(zone):
    cpu = psutil.cpu_percent() / 100
    Red = int(cpu * 255)
    Blue = int(255 - (cpu * 255))
    set_color(zone, Red, 0,  Blue)

def set_skull(zone, low, high):
    temp = psutil.sensors_temperatures()["coretemp"][0][1]
    percent_of_threshold = ((temp - low) / (high - low))
    Red = int(percent_of_threshold * 255)
    Blue = int(255 - (percent_of_threshold * 255))
    set_color(zone, Red, 0,  Blue)

def set_right(zone):
    ram_percent = (psutil.virtual_memory()[0] - psutil.virtual_memory()[1]) / psutil.virtual_memory()[0]
    Red = int(ram_percent * 255)
    Blue = int(255 - (ram_percent * 255))
    set_color(zone, Red, 0,  Blue)


#################################################################
# Taters
logger = logging.getLogger('systemd')
logger.addHandler(journal.JournalHandler())
logger.info("LED Controller starting")

startup_leds()
while True:
    set_eyes(zones["skull"])
    set_skull(zones["eyes"], cpu_temp_low, cpu_temp_high)
    set_right(zones["right_led"])
    #print("Memory usage percent is: %s" % (str(psutil.virtual_memory()[2])))
    #print("")
    time.sleep(0.1)
