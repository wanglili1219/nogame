#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import Util
from UserInfo import *
from Logger import *
import PBApp_pb2

class S2CUserInfo:
    def handle(self, respByte):
        msg = PBApp_pb2.S2CUserInfo()
        msg.ParseFromString(respByte)
        UserInfo.setId(msg.userId)
        UserInfo.setName(msg.userName)
        UserInfo.dump()
        Logger.i("user Id" + str(msg.userId))
        Logger.i("user Name " +  msg.userName)
