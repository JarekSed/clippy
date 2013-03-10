#!/usr/bin/env python

import subprocess
from time import sleep
import random
import string

import gtk,gobject
import egg.trayicon

def swap_keys():
	swap_command = 'xmodmap -e "keycode {code} = {key}"'
	get_command = 'xmodmap -pk | grep "({key})"'

	alphanum = string.lowercase + string.digits
	key1 = random.choice(alphanum)
	key2 = random.choice(alphanum)

	get_code1 = subprocess.Popen(get_command.format(key=key1), shell=True, stdout=subprocess.PIPE)
	get_code2 = subprocess.Popen(get_command.format(key=key2), shell=True, stdout=subprocess.PIPE)

	code1 = get_code1.stdout.read().split()[0]
	code2 = get_code2.stdout.read().split()[0]

	print 'swapping {key1} and {key2}'.format(key1=key1, key2=key2)

	subprocess.Popen(swap_command.format(code=code2,key=key1), shell=True)
	subprocess.Popen(swap_command.format(code=code1,key=key2), shell=True)

def swap_callback(widget, ev):
	if random.random() < 0.75:
		try:
			swap_keys()
		except:
			pass
	return True

def main():

	tray = egg.trayicon.TrayIcon("TrayIcon")
	box = gtk.EventBox()
	label = gtk.Label("clippy goes here")
	box.add(label)
	tray.add(box)
	tray.show_all()

	box.connect("button-press-event", swap_callback)

	gobject.timeout_add(30*1000, swap_callback)

	gtk.main()

if __name__ == '__main__':
	main()
