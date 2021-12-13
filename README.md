# Arturia Keystep Essential MIDI Control Center

This is an open source version of the Arturia MIDI Command Center software for the customizable hardware components on the Keystep Essential product line.

## What does it do?

Whelp, for one it runs on a Linux audio workstation with PipeWire, so that's good. It's designed for the Ardour DAW.

It has a surface mapping file for Ardour which will provide all the DAW Command Center controls on the front panel, along with the first 8 banks of fader/pan controls and one master fader/pan for the 9th.

It also might have some unlocked features *not available in the vendor published software.* So far it seems like that's limited to controlling the aftertouch range of the 8 pads.

## How do I run it?

The author is developing it on Ubuntu Studio with the latest Plasma 5 desktop release. They also have a custom built PipeWire so there's no JACK/ALSA bridging, which is weird but it works good for me.

It depends on the rtmidi C++ library and Python bindings, which are available in Ubuntu Studio, though not for the author's setup. For this reason they are compiling rtmidi manually.

After those two challenges, it should "just work" on Python 3.9

## How do I make custom hardware configs?

**none of this actually works right now**

It's easy! Open the file ardour-map-export.json in a text editor and change the values to what you want.

Just kidding, that's not easy at all. There is no UI right now. We'll get to that later. The JSON should have descriptive names that map to the same grammar as in the vendor software, so you could type values and restart the program.

If that makes sense, start the program and look at the output of `jack_lsp` or run Carla or sumn and you'll see a patch point for the MIDI output of this program! Connect it to the first Arturia hardware input (the second one does ???) and it should "just work".
