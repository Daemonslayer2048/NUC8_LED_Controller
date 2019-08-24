#! /usr/bin/python3
#################################################################
# Imports
import time

#################################################################
# Globals
acpi = "/proc/acpi/nuc_led"
zones = {
    "power": "0",
    "skull": "2",
    "eyes ": "3",
    "left_led": "4",
    "center_led": "5",
    "right_led": "6"
}
#################################################################
# Functions
def set_red(zone):
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,1,255\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,2,0\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,3,0\n")

def set_green(zone):
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,1,0\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,2,255\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,3,0\n")

def set_blue(zone):
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,1,0\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,2,0\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,3,255\n")

def set_off(zone):
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,1,0\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,2,0\n")
    with open(acpi, "w") as color:
        color.write("set_indicator_value," + zone + ",1,3,0\n")

#################################################################
# Taters
for i in range (1, 100):
    for k, v in zones.items():
        print("Zone: " + k)
        set_red(v)
        time.sleep(0.1)
        set_green(v)
        time.sleep(0.1)
        set_blue(v)
        time.sleep(0.1)
