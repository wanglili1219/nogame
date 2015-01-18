#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import PBMessage_pb2
import base

class C2SBase(object):
    def __init__(self, commandParam):
        pass

    def wrapMsgDesc(self, msg):
        md = PBMessage_pb2.MsgDesc()
        md.msgName = msg.__class__.__name__
        if not App.App.UserInfo.id:
            App.App.UserInfo.id = 0

        if not App.App.UserInfo.token:
            App.UserInfo.token = ""

        md.userId = App.UserInfo.id
        md.token = App.UserInfo.token
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

