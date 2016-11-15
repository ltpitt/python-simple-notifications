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
  notifications.py --email <subject> <message> <recipients>
  notifications.py --pushbullet <title> <message>
  notifications.py --pushover <message>
"""

import requests
import json
import sys
import httplib, urllib
from email.mime.text import MIMEText
import smtplib
server = smtplib.SMTP()
import notification_config
import docopt

def send_email(email_subject, notification_msg, email_recipients):
    '''
    This functions sends a notification using Email
            Args:
            email_subject (str) : Email Subject.
            notification_msg (str) : Email Body.
            email_recipients (str) : Email recipients.
    '''
    server.connect(notification_config.EMAIL_SERVER, notification_config.EMAIL_SERVER_PORT)
    if notification_config.EMAIL_DEBUG_LEVEL == '1':
        server.set_debuglevel(1)
    recipients = [email_recipients]
    msg = MIMEText(notification_msg)
    msg['Subject'] = email_subject
    msg['From'] = notification_config.EMAIL_SENDER
    msg['To'] = ', '.join(recipients)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(notification_config.EMAIL_SENDER, notification_config.EMAIL_PASSWORD)
    server.sendmail(notification_config.EMAIL_SENDER, recipients, msg.as_string())
    server.quit()


def send_pushover_notification(body):
    '''
    This functions sends a notification using Pushover
        Args:
            body (str) : Body of text.
    '''
    conn = httplib.HTTPSConnection("api.pushover.net")
    conn.request("POST", "/1/messages.json",
      urllib.urlencode({
        "token": notification_config.PUSHOVER_APP_TOKEN,
        "user": notification_config.USER_KEY,
        "message": body,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    response = conn.getresponse()
    if response.status != 200:
        raise Exception('Something wrong')
    else:
        print 'Sending complete'


def send_pushbullet_notification(title, body):
    '''
    This function sends a notification using Pushbullet
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    '''
    data_send = {"type": "note", "title": title, "body": body}
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + notification_config.PUSHBULLET_APP_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print 'Sending complete'


if __name__ == '__main__':
    print "Simple Notifications\n"
    arguments = docopt.docopt(__doc__, version='0.7')
    if arguments['--email']:
        send_email(arguments['<subject>'], arguments['<message>'], arguments['<recipients>'])
    elif arguments['--pushover']:
        send_pushover_notification(arguments['<message>'])
    elif arguments['--pushbullet']:
        send_pushbullet_notification(arguments['<title>'], arguments['<message>'])
