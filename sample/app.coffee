Titanium.UI.backgroundColor = 'white'
Titanium.include 'sub/sub.js'

onOpen = (e) ->
	alert 'window opened'

win = Titanium.UI.createWindow(winargs)
win.addEventListener 'open', onOpen
win.open()
