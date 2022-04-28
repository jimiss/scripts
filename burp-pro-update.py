#!/usr/bin/python3
#
# All credits go to Brian McDermott's 2020 original script (https://github.com/dev-0x0/useful-scripts/blob/main/burpsuite_update.py)
# I only modified the code to download Pro version and changed the default location
# Does not affect configuration/saved files or license keys
# 
# Downloads the latest burpsuite Pro JAR file and saves it to /opt/BurpSuitePro/burpsuite_pro.jar (the default location at time of writing for Linux)
# Renames original JAR file to .OLD for safety purposes
# EXTREMELY likely to break in the future as Portswigger make any changes to their download page etc.
# Requires SUDO privileges to write into /opt
#
# DISCLAIMER:
# NEVER run code from github on your machine without making
# sure you know what it does first. I'm not responsible for any
# loss or damage incurred by running this script. Enjoy!
#
#

import os
import sys
import requests
import shutil
from bs4 import BeautifulSoup

LATEST_VER_URL = "https://portswigger.net/burp/releases/professional/latest"
DOWNLOAD_URL = "https://portswigger-cdn.net/burp/releases/download?product=pro&version={}&type=Jar"

html = requests.get(LATEST_VER_URL)

if html.status_code != 200:
    raise("[!] Could not reach site "+BASE_URL)
    sys.exit(0)

print("[*] DISCLAIMER: Please read how the script works - not responsible for damages")
print("[*] You need to use sudo to run script and write into /opt...")
print("[*] Make sure you delete the .old file when Burp runs successfully...")
print("[*] Accessed Portswigger Download Page...")

# Parse html with bs4
content = BeautifulSoup(html.text, features="lxml")

if not content:
    raise("[!] Error parsing site content...")
    sys.exit(0)

print("[*] Latest BurpSuite Pro version: ", end="")
# get latest burp version from page text
version_heading = content.find('div', {'class': 'post-card'}).find_next('h1')
latest_version = version_heading.text[25:]
print(latest_version)

print("[*] Wgetting now ...")

# concatentate final download link
download_link = DOWNLOAD_URL.format(latest_version)

os.chdir("/opt/BurpSuitePro/")

# backup current jar just in case
os.system("rm burpsuite_pro.jar.old 2>/dev/null")
os.system("mv burpsuite_pro.jar burpsuite_pro.jar.old")
os.system("wget -O burpsuite_pro.jar {}".format(download_link))
