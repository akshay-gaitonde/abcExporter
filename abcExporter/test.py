import maya.cmds as cmds
import maya.standalone as ms

ms.initialize("python")
cmds.file("D:/akshay/modle/gearCreator_test.ma", force=True,open=True)
cams=cmds.ls(cameras=True)
for cam in cams:
    if cmds.getAttr(cam+".renderable"):
        print cam +"---> is renderable "