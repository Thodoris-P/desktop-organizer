#!usr/bin/python3
# right now only supports *.txt files


import os, shutil, getpass
from pathlib import Path

def remove_extension(filename):
	return os.path.basename(os.path.splitext(filename)[0])

def get_path(variable):
	return ('/home/' + getpass.getuser() + '/' + variable + '/')

def get_dest(new_filename, index):
	return Path(get_path('Documents') + new_filename + str(index) + '.txt')
													


for filename in os.listdir(get_path('Desktop')):
	if filename.endswith('.txt'):
		for index in range(0, 100):
			if index == 0:
				index = ''
			else:
				index += 1
			new_filename = remove_extension(filename)
			my_file = get_dest(new_filename, index)
			if my_file.is_file() == False:
				shutil.copy(filename, get_path('Documents') + new_filename 
													+ str(index) + '.txt')
				break
