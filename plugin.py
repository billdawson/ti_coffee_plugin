#!/usr/bin/env python
"""
Copyright 2011 William Dawson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---------------------------------------------------------------------------

ti_coffee_plugin/plugin.py

A simple Titanium project build plugin that will scan your Resources folder
for any .coffee files and invoke "coffee -c" on them, producing .js files with
the same base name.

See README.md for a longer description.
"""

import os, sys, subprocess

def err(s):
	# Matches the [ERROR]... messages of the Titanium builder.py, so the
	# message can be recognized as an error for console purposes
	print "[ERROR] %s" % s

def info(s):
	# Matches the [INFO]... messages of the Titanium builder.py, so the
	# message can be recognized as an info msgs for console purposes
	print "[INFO] %s" % s

def build_coffee(path):
	command_args = ['coffee', '-b', '-c', path]
	process = subprocess.Popen(command_args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	result = process.wait()
	if result != 0:
		msg = process.stdout.read()
		if msg:
			err("%s (%s)" % (msg, path))
		else:
			err("CoffeeScript compiler call for %s failed but no error message was generated" % path)

def build_all_coffee(path, simulate=False):
	info_msg_shown = False
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith('.coffee'):
				if simulate:
					print "Would build: %s" % os.path.join(root, name)
				else:
					if not info_msg_shown:
						info("Compiling CoffeeScript files")
						info_msg_shown = True
					build_coffee(os.path.join(root, name))


def compile(config):
	build_all_coffee(os.path.join(config['project_dir'], 'Resources'))

if __name__ == "__main__":
	simulate = "--simulate" in sys.argv
	cwd = os.getcwd()
	path = os.path.join(cwd, '..', '..', 'Resources')
	path = os.path.normpath(path)
	if simulate:
		print "Root: " + path
	build_all_coffee(path, simulate)

