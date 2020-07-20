Written: 20.07.2020 Emil B. Børsting
This script is meant to run on Raspberry Pi. Only tested on Pi 3B.

Keep in mind that this script is used for our retail store
that uses MSSQL server with our tables and columns and the
script needs to be tweaked (rename some values and rewrite some lines) to work on your system.
Remember to connect a USB barcode scanner to the pi and your all good!


1. Download Raspberry Pi OS 32 bit and write to sd-card.


2. Bott pi, configure pi to connect wifi, enable auto-login, enable ssh-daemon and to set correct time.
sudo raspi-config


3. Update system
sudo apt update && apt upgrade -y


4. change password for pi user
passwd


5. Install dependencies needed to run script
sudo apt install unixodbc
sudo apt install unixodbc-dev
sudo apt install freetds-dev
sudo apt install tdsodbc
sudo apt install freetds-bin
sudo apt install python3-pip
pip3 install --user pyodbc
pip3 install --user gpiozero
pip3 install --user RPi.GPIO


6. Add at bottom of FreeTDS conf file:
sudo nano /etc/freetds/freetds.conf

Add this text to the bottom of the file..
###########################################################
[sqlserver]
      host = 192.168.1.22	# Remote Sql Server's IP addr
      port = 1433		# this is default port, you can change it if needed
      tds version = 7.4		# this is the Free-TDS version by the time I write this
      instance = DB_Name	#  Database name
###########################################################


7. Create DSN (add to file)
sudo nano /etc/odbcinst.ini

Add this text to the file..
###########################################################
[FreeTDS]
Description = FreeTDS unixODBC Driver
Driver = /usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
Setup = /usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
UsageCount = 1

###########################################################
sudo nano  /etc/odbc.ini


Add this text to the file..
###########################################################
[FreeTDS]
Driver = /usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
Description = MSSQL Server
Trace = No
Server = 192.168.1.22	# IP or host name of the Sql Server
Database = DB_Name	# DataBase Name
Port = 1433		# This is default port, change if needed
TDS_Version = 7.4	# this is the Free-TDS version by the time I write this
###########################################################


8. Make boot script (add to bottom):
nano .bashrc

Add this text to the bottom of the file..
###########################################################
python3 /home/pi/update_shelf.py
###########################################################



optional...
#################
Make boot script to run after boot -> for multi-user (systemd)
nano nameofscript.py
	write the script....


nano nameofscript.service
[Unit]
Description=what script does
After=multi-user.target

[Service]
User=pi
Group=pi
WorkingDirectory=/home/pi/
Type=simple
ExecStart=/usr/bin/python3 /home/pi/nameofscript.py
KillMode=process

[Install]
WantedBy=multi-user.target


sudo cp nameofscript.service /etc/systemd/system/nameofscript.service
sudo systemctl enable update_shelf.service
####################



Links used to gather info:
https://www.it-admins.com/raspberry-pi-and-microsoft-sql-databases/
http://www.pymssql.org/_mssql_examples.html
https://raspberrypi.stackexchange.com/questions/60792/install-python-module-pyodbc-on-pi
https://stackoverflow.com/questions/57269988/unable-to-get-odbc-driver-17-for-sql-server-on-raspbian-10-buster
https://www.raspberrypi.org/forums/viewtopic.php?t=16120
https://python-tds.readthedocs.io/en/latest/pytds.html
https://gist.github.com/rduplain/1293636
https://pymssql.readthedocs.io/en/latest/index.html#
https://github.com/facebook/prophet/issues/418
https://stackoverflow.com/questions/44969924/querying-mssql-server-2012-from-a-raspberry-pi-3-using-python-freetds-and-pyodb
https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Linux
