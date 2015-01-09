#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import UserInfo

from Logger import * 
from C2SUserInfo import *
from S2CUserInfo import *
from C2SLogin import *
from S2CLogin import *
from S2CHeroInfo import *
from S2CEquipInfo import *

handlerDict = {}
handlerDict["S2CLogin"] = globals()["S2CLogin"]
handlerDict["S2CUserInfo"] = globals()["S2CUserInfo"]
handlerDict["S2CHeroInfo"] = globals()["S2CHeroInfo"]
handlerDict["S2CEquipInfo"] = globals()["S2CEquipInfo"]

def dispatch(respByte):
    md = PBMessage_pb2.MsgDesc()
    md.ParseFromString(respByte)
    if md.errorCode != 0:
        Logger.e("respone error code " + str(md.errorCode) + "," + md.errorDesc)
        return

    inst = handlerDict[md.msgName]()
    inst.handle(md.msgBytes)

    


