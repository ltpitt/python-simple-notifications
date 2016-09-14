# Notification
A tiny Python module to send out Email and push notifications (Pushover, Pushbullet) from your applications

## How to use it
* Python (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great get it from here: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder
* If you have **pip** skip to next step. You need it to easily install requirements, if you do not have it you can install it using this tutorial: https://pip.pypa.io/en/latest/installing.html 
* Run this command to install requirements: pip install -r requirements.txt
* Customize the variables at the beginning of notification.py with your Email / Pushbullet / Pushover data

You are now good to go!

Run from command line:  
python notification.py

Email Example:     --email "Email Subject", "Email Message", "Email recipients"  
Pusbullet Example: --pushbullet "Title", "Message"  
Pushover Example:  --pushover "Message"  
