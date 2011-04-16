#!/usr/bin/env python

import os

def build_coffee(path):
	pass

def build_all_coffee(path, simulate=False):
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith('.coffee'):
				if simulate:
					print "Would build: %s" % os.path.join(root, name)
				else:
					build_coffee(os.path.join(root, name))


def compile(config):
	build_all_coffee(os.path.join(config.project_dir, 'Resources'))

if __name__ == "__main__":
	# simulate
	cwd = os.getcwd()
	path = os.path.join(cwd, '..', '..', 'Resources')
	path = os.path.normpath(path)
	print "Root: " + path
	build_all_coffee(path, simulate=True)

