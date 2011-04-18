# [CoffeeScript][] -> Javascript compiler plugin for Titanium Projects.

The ti_coffee_plugin simply scans your Titanium project's `Resources` folder at build time and looks for files with the `.coffee` extension. When it finds such files, it runs the CoffeeScript compiler (`coffee -c`) to produce a Javascript file of the same name.  E.g., `win.coffee` would become `win.js`.

# Setup

## Python

Requires Python 2.5, because the `hashlib` module is used.

## CoffeeScript

First, of course, you'll need the `coffee` command available on your system.  If you can't go out to a command-line/terminal and successfully execute `coffee`, then be sure to setup [CoffeeScript][] correctly.

**Also**, if you're on OS X and you used Homebrew to install CoffeeScript and Node.js, GUI applications such as Titanium Developer and Titanium Studio -- which are precisely the apps that launch your Titanium project's build process and thus this plugin -- might not be able to successfully execute `coffee` because `/usr/local/bin` is not in the PATH by default for GUI apps, and changes to `~/.profile`, `/etc/paths`, etc., are not useful for GUI apps.  The easiest solution is to simply symlink `coffee` and `node` in `/usr/bin`, which is in the PATH:

    $ sudo ln -s /usr/local/bin/node /usr/bin/node
	$ sudo ln -s /usr/local/bin/coffee /usr/bin/coffee

If you'd rather not do that, you can muck around with `~/.MacOSX/environment.plist` following [Apple's instructions](http://developer.apple.com/library/mac/#qa/qa1067/_index.html).

## This Plugin

In the folder which houses your Titanium SDKs -- on OS X this would be `/Library/Application Support/Titanium`, create a `plugins/ti_coffee_plugin/1.0` folder.  Put the plugin.py from this repository into that folder.  So on OS X you would have this file:

	/Library/Application Support/Titanium/plugins/ti_coffee_plugin/1.0/plugin.py

Next, you need to tell your Titanium project to run this plugin when the Titanium build scripts build your project.

Build-time plugins for Titanium projects are invoked if the plugin is registered in the project's tiapp.xml file.  For the ti_coffee_plugin, you could do it like this:

	<!-- This is a child element of <ti:app> in tiapp.xml -->
	<plugins>
		<plugin version="1.0">ti_coffee_plugin</plugin>
	</plugins>

# Sample Application

The `sample/` folder contains a very simple `app.coffee` as a proof-of-concept.  You can copy that file into a new project, then run the project to see how it works.  To do that successfully, you'll also need to update your `tiapp.xml` following the example inside `tiapp.xml.example`.

# Disadvantages of Using This Plugin

- Your .coffee files will also end up in the application package that gets delivered to the device/simulator/emulator.  Unfortunately, the Titanium build plugins don't (currently) get notified when the packaging is about to occur.  They are just notified once: before the build begins.  Of course, your .coffee files are plain text and the packaging (at least on Android, but I imagine on iOS as well) compresses them.

- There might be implications when using the upcoming "fastdev" feature for Android, whereby only changed files are served up to the application being tested on device or in the emulator.  Because the updating of a .coffee file is not going to be useful unless the Javascript also gets generated, you would have to re-build more often that you would if you were just updating Javascript files.  The difference may not be too significant, however.  We'll see once the fastdev feature is released.

- You will not be able to take advantage of Titanium Studio's code assist features (code completion, etc.) if you're tying in CoffeeScript.

# License

The code is Copyright 2011 by William Dawson, and made available under the Apache 2.0 license.  Please see the LICENSE file that accompanies the source, and the licensing declarations at the top of each source file.

# Disclaimers

This is a private project of mine and currently **not supported** by Appcelerator!  If you have issues, please file them in the GitHub Issues section of the repository and I will try to get to them in a timely fashion.  Better yet, fork and improve!
[CoffeeScript]: http://jashkenas.github.com/coffee-script/
