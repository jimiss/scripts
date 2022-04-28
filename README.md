# Scripts
A repo for potentially useful scripts

**burp-pro-update.py** <p>A python script that aims to ease the updating process of BurpSuite PRO</p> 
<p>Downloads BurpSuite PRO jar file and renames the original one to .old for safety purposes</p> 
<p>Requires SUDO privileges to write into /opt - Tested on Ubuntu 20.04 - Not responsible for damages</p>
Based on original <a href="https://github.com/dev-0x0/useful-scripts/blob/main/burpsuite_update.py">script</a> of Brian McDermott aka dev-0x0 which aimed to download the community version

## Execution
```bash
wget https://raw.githubusercontent.com/jimiss/scripts/main/burp-pro-update.py
chmod +x burp-pro-update.py
sudo ./burp-pro-update.py
```
