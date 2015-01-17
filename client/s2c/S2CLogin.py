#!/usr/bin/env python

from Util import *
import UserInfo
import Logger
import PBCommand_pb2
import event

class S2CLogin:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CLogin()
        msg.ParseFromString(respByte)
        UserInfo.token = msg.token
        UserInfo.id    = msg.userInfo.userId
        UserInfo.name  = msg.userInfo.userName
        UserInfo.level = msg.userInfo.level
        UserInfo.exp   = msg.userInfo.exp
        UserInfo.gold  = msg.userInfo.gold
        UserInfo.gem   = msg.userInfo.gem

        UserInfo.dump()
        event.EventDispatcher().fire(event.EventDefine.USER_INFO_CHANGE)
        

        
