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

import os, sys, subprocess, hashlib

try:
	import json
except:
	import simplejson as json

# The Titanium build scripts contain their own json library (Patrick Logan's),
# so we have to figure out which json functions to use.
json_read = None
json_write = None
if hasattr(json, 'loads'):
	json_read = json.loads
else:
	json_read = json.read
if hasattr(json, 'dumps'):
	json_write = json.dumps
else:
	json_write = json.write

HASHES_FILE = 'coffee_file_hashes.json'
ERROR_LOG_PREFIX = '[ERROR]'
INFO_LOG_PREFIX = '[INFO]'
DEBUG_LOG_PREIX = '[DEBUG]'

def log(prefix, msg):
	print "%s %s" % (prefix, msg)

def err(msg):
	# Matches the [ERROR]... messages of the Titanium builder.py, so the
	# message can be recognized as an error for console purposes
	log(ERROR_LOG_PREFIX, msg)

def info(msg):
	# Matches the [INFO]... messages of the Titanium builder.py, so the
	# message can be recognized as an info msgs for console purposes
	log(INFO_LOG_PREFIX, msg)

def debug(msg):
	# Matches the [DEBUG]... messages of the Titanium builder.py, so the
	# message can be recognized as an debug msgs for console purposes
	log(DEBUG_LOG_PREIX, msg)

def read_file_hashes(path):
	hashes_file = os.path.join(path, HASHES_FILE)
	hashes = {}
	if os.path.exists(hashes_file):
		f = open(hashes_file, 'r')
		text = f.read()
		f.close()
		if len(text):
			hashes = json_read(text)
	return hashes

def write_file_hashes(path, hashes):
	hashes_file = os.path.join(path, HASHES_FILE)
	text = json_write(hashes)
	f = open(hashes_file, 'w')
	f.write(text)
	f.close()

def get_md5_digest(path):
	f = open(path, 'r')
	contents = f.read()
	f.close()
	return hashlib.md5(contents).hexdigest()

def build_coffee(path):
	debug('Compiling %s' % path)
	command_args = ['coffee', '-b', '-c', path]
	process = subprocess.Popen(command_args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	result = process.wait()
	if result != 0:
		msg = process.stderr.read()
		if msg:
			err("%s (%s)" % (msg, path))
		else:
			err("CoffeeScript compiler call for %s failed but no error message was generated" % path)
		return False
	return True

def build_all_coffee(path, build_path):
	info_msg_shown = False
	file_hashes = read_file_hashes(build_path)
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith('.coffee'):
				if not info_msg_shown:
					info("Compiling CoffeeScript files")
					info_msg_shown = True
				file_path = os.path.join(root, name)
				digest = get_md5_digest(file_path)
				if (not file_path in file_hashes) or (
							file_hashes[file_path] != digest):
					if build_coffee(file_path):
						file_hashes[file_path] = digest
	write_file_hashes(build_path, file_hashes)


def compile(config):
	build_all_coffee(os.path.join(config['project_dir'], 'Resources'), os.path.abspath(os.path.join(config['build_dir'], '..')))

