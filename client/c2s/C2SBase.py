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
        if not UserInfo.info.id:
            UserInfo.info.id = 0

        if not UserInfo.info.token:
            UserInfo.info.token = ""

        md.userId = UserInfo.info.id
        md.token = UserInfo.info.token
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

