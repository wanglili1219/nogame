#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from Logger import * 

from C2SUserInfo import *
from S2CUserInfo import *
from C2SLogin import *
from S2CLogin import *
from UserInfo import *


handlerDict = {}
handlerDict["S2CLogin"] = globals()["S2CLogin"]
handlerDict["S2CUserInfo"] = globals()["S2CUserInfo"]

def dispatch(respByte):
    md = PBApp_pb2.MsgDesc()
    md.ParseFromString(respByte)
    if md.errorCode != 0:
        Logger.e("respone error code " + str(md.errorCode) + "," + md.errorDesc)
        return

    inst = handlerDict[md.msgName]()
    try:
        inst.handle(md.msgBytes)
    except Exception, e:
        print "handle message", e


