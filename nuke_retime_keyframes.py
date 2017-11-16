from math import ceil

previous_fps = 24.0
new_fps = 60.0

frame_offset = new_fps / previous_fps

for node in nuke.selectedNodes():
    if node.Class() == "Transform":
        animCurves = node.knob("translate").animations()
        animCurves.append(node.knob("rotate").animation(0))
        for curve in animCurves:
            keyframes = curve.keys()
            keyframeValues = []
            for key in keyframes:
                keyframeValues.append([ceil(key.x * frame_offset), key.y])
            print keyframeValues
            curve.clear()
            for newkey in keyframeValues:
                curve.setKey(newkey[0], newkey[1])