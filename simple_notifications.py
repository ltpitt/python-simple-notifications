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
  simple_notifications.py --email <subject> <message> <recipients> [<attachments>]
  simple_notifications.py --pushbullet <title> <message>
  simple_notifications.py --pushover <title> <message>

Note:
If you have multiple email recipients or attachments use comma to separate items
python simple_notifications.py --email "Put subject here" "Put email message here"
"firstEmail@example.com, secondEmail@example.com" "LICENSE, README.md"

"""

# Import config data
import simple_notifications_config

# Import requests library, used for Pushbullet and Pushover notifications
import requests

# Import json library, used for Pushbullet notifications
import json

# Import docopt, used to generate help message and parse parameters
import docopt

# Import libraries used for email notifications
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def send_email(email_subject, email_message, email_recipients, email_attachments):
    '''
    This functions sends a notification using Email
            Args:
            email_subject     (str) : Email Subject.
            email_message     (str) : Email Body.
            email_recipients  (str) : Email recipients.
            email_attachments (str) : Email attachments.
    '''
    msg = MIMEMultipart()
    msg["From"] = simple_notifications_config.EMAIL_SENDER
    email_recipients = [email_recipients]
    msg['To'] = ', '.join(email_recipients)
    msg["Subject"] = email_subject
    msg.attach(MIMEText(email_message))

    if email_attachments is not None:
        email_attachments = email_attachments.split(",")
        for email_attachment in email_attachments:
            email_attachment = email_attachment.strip()
            ctype, encoding = mimetypes.guess_type(email_attachment)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"
            maintype, subtype = ctype.split("/", 1)
            if maintype == "text":
                fp = open(email_attachment)
                # Note: we should handle calculating the charset
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "image":
                fp = open(email_attachment, "rb")
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "audio":
                fp = open(email_attachment, "rb")
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(email_attachment, "rb")
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", "attachment", filename=email_attachment)
            msg.attach(attachment)

    server = smtplib.SMTP(simple_notifications_config.EMAIL_SERVER + ":" +
                          simple_notifications_config.EMAIL_SERVER_PORT)
    if simple_notifications_config.EMAIL_DEBUG_LEVEL == '1':
        server.set_debuglevel(1)
    server.starttls()
    server.login(simple_notifications_config.EMAIL_SENDER,simple_notifications_config.EMAIL_PASSWORD)
    server.sendmail(simple_notifications_config.EMAIL_SENDER, email_recipients, msg.as_string())
    server.quit()


def send_pushover_notification(title, message):
    '''
    This functions sends a notification using Pushover
        Args:
            title (str) : Title of notification.
            message (str) : Message of notification.
    '''
    params = {
        'token': simple_notifications_config.PUSHOVER_APP_TOKEN,
        'user': simple_notifications_config.USER_KEY,
        'title': title,
        'message': message
        }
    response = requests.post('https://api.pushover.net/1/messages.json', data=params)
    print json.dumps(params)
    if response.status_code != 200:
        print ('Something went wrong...')
        print response.content
    else:
        print 'Sending complete'


def send_pushbullet_notification(title, message):
    '''
    This function sends a notification using Pushbullet
        Args:
            title (str)    : Title of notification.
            message (str)  : Message of notification.
    '''
    params = {"type": "note", "title": title, "body": message}
    response = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(params),
                         headers={'Authorization': 'Bearer ' + simple_notifications_config.PUSHBULLET_APP_TOKEN,
                                  'Content-Type': 'application/json'})
    if response.status_code != 200:
        print ('Something went wrong...')
        print response.content
    else:
        print ('Sending complete')


if __name__ == '__main__':
    print "Simple Notifications\n"
    arguments = docopt.docopt(__doc__, version='0.7')
    if arguments['--email']:
        send_email(arguments['<subject>'], arguments['<message>'], arguments['<recipients>'],
                   arguments['<attachments>'])
    elif arguments['--pushover']:
        send_pushover_notification(arguments['<title>'], arguments['<message>'])
    elif arguments['--pushbullet']:
        send_pushbullet_notification(arguments['<title>'], arguments['<message>'])
