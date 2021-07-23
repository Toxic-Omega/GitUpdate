import os
import time

print('Installing Stuff...')
os.system('apt update && apt upgrade -y')
os.system('apt install git mitmproxy unzip apache2 -y')
print('Downloading GitUpdate Repository')
os.system('rm -r GitUpdate')
os.system('git clone https://github.com/Toxic-Omega/GitUpdate')
os.system('cp GitUpdate/SetDNS.service /etc/systemd/system/')
os.system('cp GitUpdate/SwitchProxy.service /etc/systemd/system/')
os.system('rm -r /var/www/html')
os.system('cp -r GitUpdate/html /var/www')
