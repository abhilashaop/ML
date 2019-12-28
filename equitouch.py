#!/usr/bin/python3
import os 
fname = input("")
if os.path.exists(fname):
	try:
		os.utime(fname,None)
	except OSError:
		pass
else:
	open(fname,'w+').close()
	os.utime(fname,None)
		

