# Voku :tv:

Siri → Roku TV API

- Open different apps and switch inputs
- Control volume/Toggle mute
- Fuzzy matching for pronunciation inconsistencies
- Tested with TCL Roku TVs
- Should work with any Roku-enabled Smart TV
- After setting up the shortcut, should be able to work with Homepod/Homepod mini


## Installation

### Configuration

Set the following values in ```config.py```:

- ```app_dict``` and ```input_dict``` with the key being whatever you want to say to Siri and the value as the app_id coming from ```<Roku_TV_IP>:8060/query/apps```.
- ```roku_ip``` as your TV's local IP address.

Ex. 

```python
app_dict = {
	"hulu": 2285,
	"netflix": 12,
	"youtube": 837
}

input_dict = {
    "ps4": "tvinput.hdmi1",
    "switch": "tvinput.hdmi2",
    "steam": "tvinput.hdmi3"
}

roku_ip = "192.168.1.101"
```

### Server

1. Make sure you have Python 3 and [venv](https://docs.python.org/3/library/venv.html) installed.
2. Create a virtual environment ```python3 -m venv voku_venv``` and activate it.
3. Run ```pip install -r requirements.txt``` to install all dependencies.
4. Change run.sh to use your current directory structure
5. Now we have it set up to be invoked through Siri.



### iPhone/iPad with iOS 13 Shortcuts

You can either fill in the pre-created [Apple Shortcuts link](https://www.icloud.com/shortcuts/8e8b7434df804b62a44176ffdf2b380d) (must have "Allow Untrusted Shortcuts" toggled under Shortcuts settings) or you can recreate it based off the below image:

<img src="https://raw.githubusercontent.com/phosphotungstic/voku/main/shortcut.png" width="300px">

Steps to recreate:

- Dictate Text
- Replace " " (space) with "+" in Dictated Text
- Run script over SSH
  - Host: IP of server running your Python script
  - User: Username to log in through ssh
  - Auth: Password/SSH Key, whichever you use on your server
  - Input: Leave blank
  - Script: ```</path/to/run.sh>``` Updated Text



## Usage

Launch Siri (through hardware button or "Hey Siri") and say

**"Run Roku"**

Siri will respond

**"What text"**

You reply with your command

Siri will then send your request to the server and respond with

**"Done"**



### Keywords

- ```press + <command> + (opt) <number of times>```

Presses a certain button  a specified number of times

Possible commands: ```['back', 'backspace', 'down', 'enter', 'forward', 'home', 'info', 'left', 'play', 'replay', 'reverse', 'right', 'search', 'select', 'up']```

Past 10 times, we fuzz best effort.

Ex. "press down four", "press backspace twenty"




- ```open + <app_dict key>```

Opens the app specified

Ex. "open hulu", "open netflix", etc.




- ```input + <input_dict key>```

Opens the input specified

Ex. "input ps4", "input switch"




- ```type + <any string>```

Types any string out on the Roku.

Ex. "type hello world", "type cute cat videos"




- ```power + <on/off>```

Turns the Roku on/off

Ex. "power on", "power off"




- ```volume + <up/down/mute> + <value>```

Changes Roku volume up/down a certain value or toggles mute.

Ex. "volume up fifteen", "volume down three", "volume mute"



## Planned Features
- Better support for searches/autoplay after search
- Custom keywords
- Plugins for different apps