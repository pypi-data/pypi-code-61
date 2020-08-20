#!/usr/bin/env python3
"""
TextvnCLI

Usage: 	
	texcl options FILE LINK 
	texcl options

Example:
	texcl -lo test.py testingthiscli

Options:

    -h, --help          Show help command
    --version           Show current version
    -g, --get           Copy the contents of tab to a file
    -l, --live-update   Enable live update, if the note on textvn is changed, it will be updated again with the specified file
    -o, --overwrite     Overwrite all text contents
    -w, --watch         Watch file for changes
    --remove            Remove your current credentials

"""

import os
import time
import json

from docopt import docopt
from termcolor import cprint

from textcli.update_content import Textcli
from textcli import __version__
from textcli.verify import Verify

WARNING = 'red'
MESSAGE = 'blue'
SUCCESS = 'green'

def start():
	rqn9_token = ''

	if os.path.isfile("textcli.txt"):
		with open('textcli.txt') as f:
			rqn9_token = f.read()

	arguments = docopt(__doc__, version='textcli version '+'.'.join(str(i) for i in __version__))

	filename = arguments.get('FILE', None)
	if filename is not None:
		curr_dir = os.getcwd()
		file_path = os.path.join(curr_dir, filename)

	live_update = arguments.get('--live-update', False)
	watch = arguments.get('--watch', False)

	get= arguments.get('--get', False)

	link = arguments.get('LINK', ' ')

	remove= arguments.get('--remove', False)
	
	if rqn9_token is not None and rqn9_token != '':
		try:
			rqn9_token = json.loads(rqn9_token)
		except:
			pass
	else:
		remove = False

	if rqn9_token is None or rqn9_token == '':
		try:
			cprint('Enter your RQN9 Token: ', MESSAGE)
			input1 = str(input())

			rqn9_token = {'token': input1}

			with open('textcli.txt', 'w') as f:
				f.write(str(json.dumps(rqn9_token)))
			
			verify = Verify(input1)

			if(verify.dev_info()):
				cprint('Successful!', MESSAGE)
				pass
			else:
				cprint('Invalid Token!', MESSAGE)
				remove = True


		except Exception as e:
			print(e)
			cprint("\nError: Something wrong...", WARNING)
			return 1

	elif 'token' in rqn9_token:
		pass
	
	else:
		pass

	if remove:
		try:
			if os.path.isfile("textcli.txt"):
				os.remove("textcli.txt")
				cprint("\nRemoved credential!", MESSAGE)
			else:
				cprint("\nUsage:\n\ttexcl options FILE LINK", MESSAGE)

			return 1
		except Exception as e:
			cprint("\nError: Something wrong...", WARNING)
			return 1


	try: 

		cprint('Connecting to notevn.com....', MESSAGE)

		if live_update:
			cprint("\nLive update enabled!...")

		if 'token' in rqn9_token:
			text = Textcli(link, rqn9_token['token'], live_update)

	except Exception as e:
		cprint("\nError: Please follow the usage...", WARNING)

		return -1


	if(get):
		if(text.haspw):
			cprint('\nPROTECTED: The given tab is password protected', MESSAGE)
		else:
			text.save_to_file(filename, True)
			cprint("Saved contents of file {} to {} succesfully".format(link, filename), SUCCESS)
			
		return 1




	if(text.haspw):
		cprint('\nPROTECTED: The given tab is password protected', MESSAGE)
	else:
		cprint("Saving {} to file {}..... \n".format(filename,link), SUCCESS)
		text.save_file(file_path, arguments['--overwrite'])

		try:

			if watch:
				cprint('Watching file {} for changes'.format(filename), MESSAGE)

			while watch:
				time.sleep(5)
				if text.check_file_change():
					cprint('\nFile changes detected', MESSAGE)
					text.save_file(file_path, True)
					cprint('File changes saved',MESSAGE)

		except  KeyboardInterrupt:

			cprint('\nClosing Textcli', MESSAGE) 



