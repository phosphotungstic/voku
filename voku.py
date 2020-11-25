from config import app_dict, input_dict, roku_ip
from roku import Roku
from fuzzywuzzy import process
import sys

choices = ["press", "open", "input", "type", "power", "volume"]
commands = ['back', 'backspace', 'down', 'enter', 'forward', 'home', 'info', 'left', 'play', 'replay', 'reverse', 'right', 'search', 'select', 'up']

lazy_num_dict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

tv = Roku(roku_ip)
words = sys.argv[1].lower().split("+")

fuzzed = process.extract(words[0], choices, limit=1)[0][0]

if fuzzed == "press":
  fuzzed_command = process.extract(words[1], commands, limit=1)[0][0]
  control = getattr(tv, fuzzed_command)
  if len(words) > 2:
    if words[2] in lazy_num_dict:
      repeat = lazy_num_dict[words[2]]
    else:
      repeat = int(words[2])
  else:
    repeat = 1
  for _ in range(repeat):
    control()
elif fuzzed == "open":
  print(app_dict[words[1]])
  app = tv[app_dict[words[1]]]
  app.launch()
elif fuzzed == "input":
  input_switch = tv[input_dict[words[1]]]
  input_switch.launch()
elif fuzzed == "type":
  orig_words = ' '.join(sys.argv[1].split("+")[1:])
  tv.literal(orig_words)
elif fuzzed == "power":
  if words[1] == "off":
    tv.poweroff()
  elif words[1] == "on":
    tv.poweron()
elif fuzzed == "volume":
  if words[1] == "mute":
    tv.volume_mute()
  else:
    if words[2] in lazy_num_dict:
      repeat = lazy_num_dict[words[2]]
    else:
      repeat = int(words[2])

    if words[1] == "down":
      for _ in range(repeat):
        tv.volume_down()
    if words[1] == "up":
      for _ in range(repeat):
        tv.volume_up()