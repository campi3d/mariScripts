import mari

def enableCommandPort():
	mari.app.enableCommandPort( not mari.app.commandPortEnabled() )
	print "command port enabled with the number", mari.app.commanPortNumber()

mari.menus.addAction(mari.actions.crete('Toggle Command Port', 'enableCommandPort()'), "MainWindow/Python")
