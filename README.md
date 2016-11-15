# Notification
A tiny Python module to send out Email and push notifications (Pushover, Pushbullet) from your applications

## How to install
* **Python** (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder
* If you have **pip** skip to next step. You need **pip** to easily install requirements, if you do not have **pip** you can install it using this tutorial: https://pip.pypa.io/en/latest/installing.html 
* Run this command (be sure to run it from notification.py folder) to install requirements: ***pip install -r requirements.txt***
* Customize the variables at the beginning of notification_config.py with your Email / Pushbullet / Pushover data
* **!!! Be sure that no other user can read notification_config.py (you need to change file's permissions to achieve this result) !!!**

You are now good to go.

## How to use notification.py from command line
If you can run from command line:    
***python notification.py***

This will produce the onscreen help:  
***Email Example:     --email "Email Subject", "Email Message", "Email recipients"***  
***Pusbullet Example: --pushbullet "Title", "Message"***  
***Pushover Example:  --pushover "Message"***  
  
Here you can find a complete command example, using email notification:  
***python notification.py --email "Notification Email Subject" "A very important message" "any@email.com"***  

## How to import notification.py in another Python script
If you prefer using the function from another Python script you can simply import notification.py (be sure that all files are in the same folder):  
```python
# This is a simple script to show how to integrate notification.py in your projects
#
# In this script I am just checking when the Trolls movie DVD will be released scaping a web page
# When it is released I will get a notification :)
#
# Feel free to customize url_to_check and string_to_check for your needs
#
#!/bin/python

import urllib2
import re
# Row below imports notification.py (be sure to save this script in the same folder to make it work)
import notification

url_to_check = 'http://www.dvdsreleasedates.com/movies/5974/Trolls-2016.html'
string_to_check = 'not announced'

html_content = urllib2.urlopen(url_to_check).read()
matches = re.findall(string_to_check, html_content);

if len(matches) == 0:
# Row below contains the notification part
   notification.send_pushover_notification(stuff_to_check + ' is now available\n\n<a href="' + url_to_check + '">Get it  now</a>')
   print '*** ' + string_to_check + ' ***' + ' - Not found in site!'
else:
   print '*** ' + string_to_check + ' ***' + ' - Found in site!'

```
