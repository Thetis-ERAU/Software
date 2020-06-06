#!bin/bash
#Installs required dependencies for Thetis & clones repo

#make sure that we have git
sudo apt-get install git

#Clone Repo
cd ~
mkdir Desktop & cd "&_"
cd Desktop
mkdir Thetis & cd "&_"
git clone https://github.com/Thetis-ERAU/Software.git

#Install dependencies
sudo apt-get update
sudo apt-get install python3
sudo apt-get install pip3
sudo pip3 install adafruit-circuitpython-gps
sudo pip3 install adafruit-circuitpython-servokit
sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-blinka
sudo pip3 insatll adafruit-circuitpython-ads1x15

#sudo apt-get install gpsd gpsd-clients python-gps p

#Enable VNC, Serial, I2C and SSH
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_vnc 0
sudo raspi-config noning do_serial 0