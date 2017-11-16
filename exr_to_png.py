nuke.selectAll()
nuke.invertSelection()

for node in nuke.allNodes():
    if "Read" in node["name"].value():
        exr_path = node["file"].value()
        png_path = exr_path.rpartition(".")[0] + ".png"
        first_frame = int(node.knob("first").value())
        last_frame = int(node.knob("last").value())
        node.knob("selected").setValue(True)
        if first_frame > 1:
             offset_node = nuke.createNode("TimeOffset")
             node.knob("selected").setValue(False)
             offset_node.knob("selected").setValue(True)
             offset_node.knob("time_offset").setValue(-first_frame+1 )
             last_frame = (last_frame - first_frame) + 1
             first_frame = 1
        write_node = nuke.createNode("Write")
        write_node.knob("file").setValue(png_path)
        write_node.knob("channels").setValue("rgba")
        nuke.execute(write_node, first_frame, last_frame)
        try:
            node.knob("selected").setValue(False)
            offset_node.knob("selected").setValue(False)
        except:
            nuke.selectAll()
            nuke.invertSelection()
