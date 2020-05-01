# Media-Server
A Raspberry-pi based system that was able to host media stored in storage device and connected to RPi onto a local network. Tools used: Python, Web server, Web development, Terminal coding, RPi

This repository consists of three python codes and two intermediary .txt files used in the process.

test.py: This file is executed in the Raspberry pi while booting to bind the external harddisk/storage device to the RPi.

tcode1.py: This file is also executed during the booting but after the test.py. This code reads the contents(movies/media) from the storage, processes on
           it to filter and categorize the data and feed it to respective folders based on categories/generes and more.
           
shutdown.py: This file is to shut down the headless Raspberry Pi with the help of a button using a GPIO pin of the raspberry pi.
