#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
#  ______________________
# / Simple Notifications \
# \ By Davide Nastri     /
#  ----------------------
#     \ ^__^
#      \(oo)\_______
#       (__)\       )\/\
#         ||-----w |
#         ||      ||
#
# This script sends push notification using
# Email, Pushbullet or Pushover
#
# Please put your data into configure.py before using this script

"""
Simple Notifications v{version}

Usage:
  simple_notifications.py --email <subject> <message> <recipients>
  simple_notifications.py --pushbullet <title> <message>
  simple_notifications.py --pushover <title> <message>
"""

import requests
import json
import sys
from email.mime.text import MIMEText
import smtplib
server = smtplib.SMTP()
import simple_notifications_config
import docopt

def send_email(email_subject, notification_msg, email_recipients):
    '''
    This functions sends a notification using Email
            Args:
            email_subject (str) : Email Subject.
            notification_msg (str) : Email Body.
            email_recipients (str) : Email recipients.
    '''
    server.connect(simple_notifications_config.EMAIL_SERVER, simple_notifications_config.EMAIL_SERVER_PORT)
    if simple_notifications_config.EMAIL_DEBUG_LEVEL == '1':
        server.set_debuglevel(1)
    recipients = [email_recipients]
    msg = MIMEText(notification_msg)
    msg['Subject'] = email_subject
    msg['From'] = simple_notifications_config.EMAIL_SENDER
    msg['To'] = ', '.join(recipients)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(simple_notifications_config.EMAIL_SENDER, simple_notifications_config.EMAIL_PASSWORD)
    server.sendmail(simple_notifications_config.EMAIL_SENDER, recipients, msg.as_string())
    server.quit()


def send_pushover_notification(title, body):
    '''
    This functions sends a notification using Pushover
        Args:
            title (str) : Title of notification.
            body (str) : Body of notification.
    '''
    params = {
        'token': simple_notifications_config.PUSHOVER_APP_TOKEN,
        'user': simple_notifications_config.USER_KEY,
        'title': title,
        'message': body,
        'retry': 30, 
        'expire': 180,
        'priority': 2,
        'sound': 'siren',
        }
    response = requests.post('https://api.pushover.net/1/messages.json', data=json_dumps(params))
    if response.status_code != 200:
        print ('Something went wrong...')
        print response.content
    else:
        print 'Sending complete'


def send_pushbullet_notification(title, body):
    '''
    This function sends a notification using Pushbullet
        Args:
            title (str) : Title of notification.
            body (str) : Body of notification.
    '''
    params = {"type": "note", "title": title, "body": body}
    response = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(params),
                         headers={'Authorization': 'Bearer ' + simple_notifications_config.PUSHBULLET_APP_TOKEN, 'Content-Type': 'application/json'})
    if response.status_code != 200:
        print ('Something went wrong...')
        print response.content
    else:
        print ('Sending complete')


if __name__ == '__main__':
    print "Simple Notifications\n"
    arguments = docopt.docopt(__doc__, version='0.7')
    if arguments['--email']:
        send_email(arguments['<subject>'], arguments['<message>'], arguments['<recipients>'])
    elif arguments['--pushover']:
        send_pushover_notification(arguments['<title>'], arguments['<message>'])
    elif arguments['--pushbullet']:
        send_pushbullet_notification(arguments['<title>'], arguments['<message>'])
