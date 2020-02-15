#!/usr/bin/env python
# -*- encoding: utf-8 -*-
try:
    # Python 2 import
    import simple_notifications_config
except Exception as ex:
    # Python 3 import    
    from . import simple_notifications_config
# Import requests library, used for Pushbullet and Pushover notifications
import requests
# Import json library, used for Pushbullet notifications
import json
# Import click, used to generate help message and parse parameters
import click
# Import libraries used for email notifications
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


@click.group()
def notification():
    '''
    Simple Notifications sends out email and push notifications from your applications (using Pushbullet or Pushover)
    '''
    pass

@notification.command(help='Send a notification using Pushover')
@click.option('--subject', help='Pushover notification subject', required=True)
@click.option('--body', help='Pushover notification body', required=True)
@click.option('--image', help='Pushover notification image', default="no")
def pushover(subject, body, image):
    '''
    This functions sends a notification using Pushover
        Args:
            subject (str) : Title of notification.
            body    (str) : Message of notification.
            image   (str) : Image filename of notification.
    '''
    click.echo('Sending out Pushover notification...')
    params = {
        'token': simple_notifications_config.PUSHOVER_APP_TOKEN,
        'user': simple_notifications_config.USER_KEY,
        'title': subject,
        'message': body
        }
    if image != "no":
        image = {"attachment": ("image.jpg", open(image, "rb"), "image/jpeg")}
        response = requests.post('https://api.pushover.net/1/messages.json', data=params, files=image)
    else:
        response = requests.post('https://api.pushover.net/1/messages.json', data=params)
    print (json.dumps(params))
    if response.status_code != 200:
        print ('Something went wrong...')
        print (response.content)
    else:
        print ('Sending complete')

@notification.command(help='Send a notification using Pushbullet')
@click.option('--subject', help='Pushbullet notification subject', required=True)
@click.option('--body', help='Pushbullet notification body', required=True)
def pushbullet(subject, body):
    '''
    This function sends a notification using Pushbullet
        Args:
            subject (str)    : Title of notification.
            body    (str)    : Message of notification.
    '''
    click.echo('Sending out Pushbullet notification...')
    params = {'type': 'note', 'title': subject, 'body': body}
    response = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(params),
                         headers={'Authorization': 'Bearer ' + simple_notifications_config.PUSHBULLET_APP_TOKEN,
                                  'Content-Type': 'application/json'})
    if response.status_code != 200:
        print ('Something went wrong...')
        print (response.content)
    else:
        print ('Sending complete')

@notification.command(help='Send a notification using Email')
@click.option('--subject', help='Email Subject', required=True)
@click.option('--body', help='Email Body', required=True)
@click.option('--recipients', help='Separate multiple recipients using comma', required=True)
@click.option('--attachments', help='Accepts complete file paths. Separate multiple attachments using comma')
def email(subject, body, recipients, attachments):
    '''
    This functions sends a notification using Email
            Args:
            subject     (str) : Email Subject.
            body        (str) : Email Body.
            recipients  (str) : Email recipients.
            attachments (str) : Email attachments.
    '''
    click.echo('Sending out Email notification...')
    msg = MIMEMultipart()
    msg['From'] = simple_notifications_config.EMAIL_SENDER
    email_recipients = [recipients]
    msg['To'] = ', '.join(email_recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    if attachments is not None:
        attachments = attachments.split(',')
        for email_attachment in attachments:
            email_attachment = email_attachment.strip()
            ctype, encoding = mimetypes.guess_type(email_attachment)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            if maintype == 'text':
                fp = open(email_attachment)
                # Note: we should handle calculating the charset
                attachments = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'image':
                fp = open(email_attachment, 'rb')
                attachments = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'audio':
                fp = open(email_attachment, 'rb')
                attachments = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(email_attachment, 'rb')
                attachments = MIMEBase(maintype, subtype)
                attachments.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachments)
            attachments.add_header('Content-Disposition', 'attachments', filename=email_attachment)
            msg.attach(attachments)

    server = smtplib.SMTP(simple_notifications_config.EMAIL_SERVER + ':' +
                          simple_notifications_config.EMAIL_SERVER_PORT)
    if simple_notifications_config.EMAIL_DEBUG_LEVEL == '1':
        server.set_debuglevel(1)
    server.starttls()
    server.login(simple_notifications_config.EMAIL_SENDER,simple_notifications_config.EMAIL_PASSWORD)
    server.sendmail(simple_notifications_config.EMAIL_SENDER, email_recipients, msg.as_string())
    server.quit()


# Uncomment these rows for manual testing
#if __name__ == '__main__':
#    notification()
