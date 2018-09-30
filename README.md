# Ping-of-Death Maker
Python script that uses the scapy library to create and send pings of death.

# Description
The python script creates an IP and ICMP packet that can be personalized editing the source and target IP. The ICMP packet is big enough to be interpreted as the Ping of Death. Test on your own networks (the ones you own), not from somebody else.

# Tested on
Kali LXDE Linux

# Before Running Install
Install Scapy. Checkout this tutorial: https://scapy.readthedocs.io/en/latest/installation.html

# Run
Execute the script with super-user permissions.
The script makes use of 'scapy' library which needs administration level to create network packets.

Usage: sudo ./pingOfDeath.py

By am0nt031r0
