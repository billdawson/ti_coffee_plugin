Titanium.UI.backgroundColor = 'white'
Titanium.include 'sub/sub.js'

open = (e) ->
	alert 'window did open'

win = Titanium.UI.createWindow(winargs)
win.addEventListener 'open', open
win.open()
