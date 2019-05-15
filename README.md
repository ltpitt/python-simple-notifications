# Simple Notifications
>Simple Notifications is a cross-platform command line tool that allows to easily send out Email (also with attachment) and push notifications (using [Pushover](https://pushover.net) or [Pushbullet](https://www.pushbullet.com))  

## Requirements
* Python. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Python Pip. Here are [installation instructions](https://pip.pypa.io/en/stable/installing/).  

## How to install

Once Python and Python Pip are installed:

    $ git clone https://github.com/ltpitt/python-simple-notifications.git
    $ cd python-github-backup
    $ pip install .

Then customize simple_notifications_config.py with the required Email / Pushbullet / Pushover configuration data.  

Example simple_notification_config.py path for a Windows 10 installation using Python 2.7:  
C:\Python27\Lib\site-packages\simple_notifications\simple_notifications_config.py  

Example simple_notification_config.py path for a Windows 10 installation using Python 3.7:  
C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python37\Lib\site-packages\simple_notifications  
  
Example simple_notification_config.py path for a Linux installation:  
/usr/local/lib/python2.7/dist-packages/simple_notifications/simple_notifications_config.py  
  
As last step remember to make the simple_notification_config.py file readable only for the user that will run the script.  
  
On Windows right click on the file, properties and then customize the permissions tab using this explanation:  
  
https://msdn.microsoft.com/en-us/library/bb727008.aspx

On Linux:
  
    $ chmod 400 /usr/local/lib/python2.7/dist-packages/simple_notifications/simple_notifications_config.py  


## Usage

To use it:

    $ simple-notifications --help
    
    
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
