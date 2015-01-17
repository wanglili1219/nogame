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
        UserInfo.info.token = msg.token
        UserInfo.info.id    = msg.userInfo.userId
        UserInfo.info.name  = msg.userInfo.userName
        UserInfo.info.level = msg.userInfo.level
        UserInfo.info.exp   = msg.userInfo.exp
        UserInfo.info.gold  = msg.userInfo.gold
        UserInfo.info.gem   = msg.userInfo.gem

        UserInfo.info.dump()
        event.EventDispatcher().fire(event.EventDefine.USER_INFO_CHANGE)
        

        
