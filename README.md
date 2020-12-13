![build](https://github.com/ltpitt/python-simple-notifications/workflows/Python%20package/badge.svg)
[![GitHub Issues](https://img.shields.io/github/issues-raw/ltpitt/python-simple-notifications)](https://github.com/ltpitt/python-simple-notifications/issues)
![Total Commits](https://img.shields.io/github/last-commit/ltpitt/python-simple-notifications)
![GitHub commit activity](https://img.shields.io/github/commit-activity/4w/ltpitt/python-simple-notifications?foo=bar)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://opensource.org/licenses/GPL-3.0)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

# Simple Notifications
>Simple Notifications is a cross-platform command line tool that allows to easily send out Email (also with attachment) and push notifications (using [Pushover](https://pushover.net) or [Pushbullet](https://www.pushbullet.com))  

## Pre-requisites
* Python: [installation instructions](https://www.python.org/downloads/).
* Python Pip: it should be available in your Python install, if this is not your case here's [installation instructions](https://pip.pypa.io/en/stable/installing/).  

## How to install

Once Python and Python Pip are installed:

    $ git clone https://github.com/ltpitt/python-simple-notifications.git
    $ cd python-simple-notifications
    $ pip install .

Then customize simple_notifications_config.py with the required Email / Pushbullet / Pushover configuration data.  It is easy to understand how if you read the comments in simple_notifications_config.py.  

Example simple_notification_config.py path for a Windows 10 installation using Python 2.7:  
`C:\Python27\Lib\site-packages\simple_notifications\simple_notifications_config.py  `

Example simple_notification_config.py path for a Windows 10 installation using Python 3.7:  
`C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python37\Lib\site-packages\simple_notifications  `
  
Example simple_notification_config.py path for a Linux installation:  
`/usr/local/lib/python2.7/dist-packages/simple_notifications/simple_notifications_config.py  `
  
As last step remember to make the simple_notification_config.py file readable only by the user that will run the script.  
  
On Windows right click on the file, properties and then customize the permissions tab using this explanation:  
  
https://msdn.microsoft.com/en-us/library/bb727008.aspx

On Linux:
  
    $ chmod 400 /usr/local/lib/python2.7/dist-packages/simple_notifications/simple_notifications_config.py  


## Usage

Here's how to display help:

    $ simple-notifications --help
    
Output:    
```bash
Usage: simple-notifications [OPTIONS] COMMAND [ARGS]...

  Simple Notifications sends out email and push notifications from your
  applications (using Pushbullet or Pushover)

Options:
  --help  Show this message and exit.

Commands:
  email       Send a notification using Email
  pushbullet  Send a notification using Pushbullet
  pushover    Send a notification using Pushover

```


### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
