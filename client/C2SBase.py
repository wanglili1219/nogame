#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from UserInfo import *
import PBApp_pb2

class C2SBase:
    def __init__(self):
        pass

    def wrapMsgDesc(self, msgName, msg):
        md = PBApp_pb2.MsgDesc()
        md.msgName = msgName
        md.userId = UserInfo.getId()
        md.token = UserInfo.getToken()
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

