# pi.hole My Custom Whitelist
![alt text](https://badgen.net/badge/platform/pi.hole/blue?) ![alt text](https://badgen.net/badge/content/whitelist/green?)

Basic Custom whitelist for pi.hole

## Description
This domine whitelist for Pi-hole collect my personal blockerd domine that I want be in whitelist

## Upload to pihole database

To configure the domain list, please follow these steps:

Download the script:
``` 
cd /opt
sudo wget https://raw.githubusercontent.com/paolo-hub/pi.hole_basic_domine_blacklist/main/pihole_domain_black.py
``` 

Execute the script:
``` 
python3 pihole_witelist_custom.py
``` 

This will load the domains with the description "My Whitelist" and place them in the Default group.
