#!/usr/bin/env python
import json
import midi
# import jack

SCREEN_TYPE = 0x04
SCREEN_CID = 0x20
CONTROLLER_TYPE = 0x20
USER_MIDI_CHANNEL = 0x41
PAD_NOTE_OFF_VELOCITY = 0x40
MAP_FILE = "ardour-map-export.json"

# A Drawbar is inverted, up = 0 down = 127
# It's an organ thing
fader_option_map = [
  {"Type": "Fader", "value" : 12},
  {"Type": "Drawbar", "value" : 13 },
]
# not sure what the three levels of relative means
knob_option_map = [
  {"Type": "Absolute", "value": 0},
  {"Type": "Relative 1", "value": 1},
  {"Type": "Relative 2", "value": 2},
  {"Type": "Relative 3", "value": 3},
]
# I think the manual defines in words what these types mean
knob_acceleration_map = [
  {"Type": "None", "value": 0},
  {"Type": "Medium", "value": 1},
  {"Type": "Fast", "value": 2},
  {"Type": "1:1", "value": 3},
]
pad_option_map = [
  {"Type": "Gate", "value" : 1},
  {"Type": "Toggle", "value" : 0},
]
pad_mode_map = [
  {"Type": "None", "value": 0},
  {"Type": "MIDI Note", "value": 7},
  {"Type": "Switched Control", "value": 8},
  {"Type": "Patch Change", "value": 9},
  {"Type": "MMC", "value": 10},
]
pad_mmc_map = [
  {"Type": "Start", "value": 2},
  {"Type": "Stop", "value": 3},
  {"Type": "Record", "value": 4},
]
