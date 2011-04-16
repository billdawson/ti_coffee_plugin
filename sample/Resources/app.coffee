Titanium.UI.backgroundColor = 'white'
Titanium.include 'sub/sub.js'

open = (e) ->
	alert 'open'

win = Titanium.UI.createWindow(winargs)
win.addEventListener 'open', open
win.open()
