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
# Email, Pushbullet or Pushover
#
# Email has been tested using smtp.gmail.com and port 587
#
# Please fill in your data and make sure this configuration file is not readable by other users

# Email notification parameters
server = smtplib.SMTP()
EMAIL_PASSWORD = 'YOUR_PASSWORD'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_SERVER_PORT = '587'
EMAIL_DEBUG_LEVEL = '1'

# Push notification parameters (Pushover)
PUSHOVER_APP_TOKEN = 'YOUR_APP_TOKEN'
USER_KEY = 'YOUR_USER_KEY'

# Push notification parameters (Pushbullet)
PUSHBULLET_APP_TOKEN = 'YOUR_APP_TOKEN'
