#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import UserInfo
import PBMessage_pb2

class C2SBase(object):
    def __init__(self):
        pass

    def wrapMsgDesc(self, msg):
        md = PBMessage_pb2.MsgDesc()
        md.msgName = msg.__class__.__name__
        if not UserInfo.id:
            UserInfo.id = 0

        if not UserInfo.token:
            UserInfo.token = ""

        md.userId = UserInfo.id
        md.token = UserInfo.token
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

