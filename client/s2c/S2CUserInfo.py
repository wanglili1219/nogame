#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import Util
import UserInfo 
import Logger
import PBCommand_pb2
import event

class S2CUserInfo:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CUserInfo()
        msg.ParseFromString(respByte)
        ui = msg.userInfo
        Logger.i(str(ui))
        UserInfo.id    = ui.userId
        UserInfo.name  = ui.userName
        UserInfo.level = ui.level
        UserInfo.exp   = ui.exp
        UserInfo.gold  = ui.gold
        UserInfo.gem   = ui.gem
        UserInfo.dump()
        event.EventDispatcher().fire(event.EventDefine.USER_INFO_CHANGE)
