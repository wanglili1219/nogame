#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import UserInfo
import os

import Logger
import c2s
from c2s import *
import s2c
from s2c import *
    
HandlerDict = {}

def dispatch(respByte):
    md = PBMessage_pb2.MsgDesc()
    md.ParseFromString(respByte)
    if md.errorCode != 0:
        Logger.e("respone error code " + str(md.errorCode) + "," + md.errorDesc)
        return

    if not HandlerDict.has_key(md.msgName):
        raise KeyError("not found " + md.msgName)

    inst = HandlerDict[md.msgName]()
    inst.handle(md.msgBytes)
    

def init():
    s2cpath = os.path.abspath('.') + "/s2c/"
    for parent, dirnames, filenames in os.walk(s2cpath): 
        for filename in filenames:
            ext = os.path.splitext(filename)[1][1:]
            basename = os.path.splitext(filename)[0]
            if ext == "py" and basename.startswith("S2C"):
                print "insert ", basename
                HandlerDict[basename] = globals()[basename]
    

    


