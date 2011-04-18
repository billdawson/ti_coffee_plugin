Titanium.UI.backgroundColor = 'white'
Titanium.include 'sub/sub.js'
winargs =
	backgroundColor: 'red'
	fullscreen: false
	title: 'Test window'
	exitOnClose: true

onOpen = (e) ->
	alert 'window opened'

win = Titanium.UI.createWindow(winargs)
win.addEventListener 'open', onOpen
win.open()
