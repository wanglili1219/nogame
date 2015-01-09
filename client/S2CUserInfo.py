#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import Util
import UserInfo 
from Logger import *
import PBCommand_pb2

class S2CUserInfo:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CUserInfo()
        msg.ParseFromString(respByte)
        ui = msg.userInfo
        UserInfo.info.id = ui.userId
        UserInfo.info.name = ui.userName
        UserInfo.info.level = ui.level
        UserInfo.info.exp = ui.exp
        UserInfo.info.gold = ui.gold
        UserInfo.info.gem = ui.gem
        UserInfo.info.dump()
