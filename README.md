# [CoffeeScript][] -> Javascript compiler plugin for Titanium Projects.

The ti_coffee_plugin simply scans your Titanium project's `Resources` folder at build time and looks for files with the `.coffee` extension. When it finds such files, it runs the CoffeeScript compiler (`coffee -c`) to produce a Javascript file of the same name.  E.g., `win.coffee` would become `win.js`.

# Setup

First, of course, you'll need the `coffee` command available on your system.  If you can't go out to a command-line/terminal and successfully execute `coffee`, then be sure to setup [CoffeeScript][] correctly.

Next, you need to tell your Titanium project to run this plugin when the Titanium build scripts build your project.

Build-time plugins for Titanium projects are invoked if the plugin is registered in the project's tiapp.xml file.  For the ti_coffee_plugin, you could do it like this:

	<!-- This is a child element of <ti:app> in tiapp.xml -->
	<plugins>
		<plugin>ti_coffee_plugin</plugin>
	</plugins>

Then put the plugin.py into the folder `plugins/ti_coffee_plugin` in your project.  Voilà, it will be invoked automatically when you build your files.

# Sample Application

The `sample/` folder contains a very simple Titanium project.  **Important**: The sample won't work unless you copy the plugin.py down into the `sample/plugins/ti_coffee_plugin/` folder.  I didn't want to put plugin.py in two places in the source tree.

# License

The code is Copyright 2011 by William Dawson, and made available under the Apache 2.0 license.  Please see the LICENSE file that accompanies the source, and the licensing declarations at the top of each source file.

# Disclaimers

This is a private project of mine and currently **not supported** by Appcelerator!  If you have issues, please file them in the GitHub Issues section of the repository and I will try to get to them in a timely fashion.  Better yet, fork and improve!
[CoffeeScript]: http://jashkenas.github.com/coffee-script/
