#!/usr/bin/env python

from Util import *
from UserInfo import *
from Logger import *
import PBApp_pb2

class S2CLogin:
    def handle(self, respByte):
        msg = PBApp_pb2.S2CLogin()
        msg.ParseFromString(respByte)
        UserInfo.setId(msg.userId)
        UserInfo.setToken(msg.token)
        Logger.i(str(msg.userId))
        Logger.i(msg.token.encode("GBK"))

        
