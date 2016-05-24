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
# This script sends notification using
# Email or Pushover
#
# It has been tested using smtp.gmail.com and port 587

import smtplib
import sys
from email.mime.text import MIMEText
import httplib, urllib

# Email notification parameters
server = smtplib.SMTP()
EMAIL_SENDER = 'YOUR_EMAIL'
EMAIL_PASSWORD = 'YOUR_PASSWORD'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_SERVER_PORT = '587'

# Push notification parameters (Pushover)
PUSHOVER_APP_TOKEN = 'YOUR_APP_TOKEN'
USER_KEY = 'YOUR_USER_KEY'


def send_email(email_subject, notification_msg, email_recipients):
    '''
    This functions sends a notification using Email
    '''
    server.connect(EMAIL_SERVER, EMAIL_SERVER_PORT)
    server.set_debuglevel(1)
    recipients = [email_recipients]
    msg = MIMEText(notification_msg)
    msg['Subject'] = email_subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = ', '.join(recipients)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, recipients, msg.as_string())
    server.quit()


def send_pushover_notification(message):
    '''
    This functions sends a notification using Pushover
    '''
    conn = httplib.HTTPSConnection("api.pushover.net")
    conn.request("POST", "/1/messages.json",
      urllib.urlencode({
        "token": PUSHOVER_APP_TOKEN,
        "user": USER_KEY,
        "message": message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()


def display_help():
    '''
    This functions displays the command help
    '''
    print 'Email Example:    --email "Email Subject", "Email Message", "Email recipients"'
    print 'Pushover Example: --pushover "Message"'


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--email":
            print len(sys.argv)
            if len(sys.argv) == 5:
                EMAIL_SUBJECT = sys.argv[2]
                EMAIL_MESSAGE = sys.argv[3]
                EMAIL_RECIPIENTS = sys.argv[4]
                send_email(EMAIL_SUBJECT, EMAIL_MESSAGE, EMAIL_RECIPIENTS)
            else:
                display_help()
        elif sys.argv[1] == "--pushover":
            if len(sys.argv) == 3:
                send_pushover_notification(sys.argv[2])
            else:
                display_help()
        else:
            display_help()
    else:
        display_help()


if __name__ == '__main__':
    main()
