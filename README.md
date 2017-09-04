# Simple Notifications
Simple Notifications is a cross-platform command line tool that allows you to easily send out Email and push notifications (Pushover, Pushbullet)  

## How to install
* **Python** (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder

Now you have two choices: pip or pipsi.  

Pip is the classic choice.  
Here are [installation instructions](https://pip.pypa.io/en/stable/installing/).  

Once pip is installed, from the script folder:

    $ pip install .

The other option is pipsi.  
If you don't use `pipsi`, you're missing out.  
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Once pipsi is installed, from the script folder: 

    $ git clone https://github.com/ltpitt/python-simple-notifications.git
    $ cd python-github-backup
    $ pipsi install .

As last step please customize simple_notifications_config.py with your email / Pushbullet / Pushover data and, obviously, chmod it so that no other user can read it  

Example folder for a Windows 10 installation:  
C:\Python27\Lib\site-packages\simple_notifications\simple_notifications_config.py  
  
Example folder for a Linux installation:  
/usr/local/lib/python2.7/dist-packages/simple_notifications/simple_notifications_config.py  

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

## How to schedule automatic script execution
* If you have Windows: https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx
* If you have Linux or Mac: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/

### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
