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
sudo wget https://raw.githubusercontent.com/paolo-hub/pi.hole_whitelist_custom/main/pihole_witelist_custom.py
``` 

Execute the script:
``` 
python3 pihole_witelist_custom.py
``` 

This will load the domains with the description "My Whitelist" and place them in the Default group.

## Automatic update every day

Open crontab:
```
crontab -e
```

Add every day execution at 5:00 am
```
# My Witelist
0 5 * * * python3 /opt/pihole_witelist_custom.py >/dev/null 2>&1
```
Then Ctrl+O for save and Ctrl+X to close

## Direct Links
|    Service        |   Link       |
| ----------------- | ------------ |
|    pi Hole        |   [link_for_piHole](https://raw.githubusercontent.com/paolo-hub/pi.hole_whitelist_custom/Whitelist_Custom.txt)     |
|    Ad Guard       |   [link_for_Ad_Guard](https://raw.githubusercontent.com/paolo-hub/pi.hole_whitelist_custom/main/adguard_whitelist_custom.txt)     |

