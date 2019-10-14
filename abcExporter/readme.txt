#code to paste and run in maya script editor

import sys
import maya.cmds as cmds

USERAPPDIR = cmds.internalVar(userAppDir=True)
exporter_path = "2017/prefs/scripts/abcExporter/"
full_path=USERAPPDIR + exporter_path
sys.path.append(full_path)


import sfui
reload(sfui)

ui=sfui.showUI()