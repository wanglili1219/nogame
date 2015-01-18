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
        UserInfo.updateFromServerData(msg.userInfo)
