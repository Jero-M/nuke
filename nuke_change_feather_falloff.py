def changeFeather(value):  
    for s in nuke.selectedNodes():
        selNode = nuke.selectedNode()
        if s.Class() == "Roto" or s.Class() == "RotoPaint":
            for item in s['curves'].rootLayer:
                attr = item.getAttributes()
                attr.set('ff',value)

feather_value = 0
changeFeather(feather_value)