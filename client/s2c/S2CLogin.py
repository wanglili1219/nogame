#!/usr/bin/env python

from Util import *
import base
import Logger
import PBCommand_pb2
import event

class S2CLogin:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CLogin()
        msg.ParseFromString(respByte)
        base.UserInfo.updateFromServerData(msg.userInfo)
        

        
