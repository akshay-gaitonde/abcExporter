import maya.cmds as cmds
import maya.standalone as ms
import sys
import os


class test():
    def __init__(self):
        pass


    def printer(self,path,cb,epi,seq,take,item):
        print "================NEW OUTPUT========================="
        print path
        print cb
        print epi
        print seq
        print take
        print item
        #self.maya_standalone()
        print "================OUTPUT Ended========================="

'''
    def maya_standalone(self):

        cmds.file("D:/akshay/modle/gearCreator_test.ma")
        cams = cmds.ls(geometry=True)
        print cams
'''