#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import PBMessage_pb2
import base
import App

class C2SBase(object):
    def __init__(self, commandParam):
        pass

    def wrapMsgDesc(self, msg):
        md = PBMessage_pb2.MsgDesc()
        md.msgName = msg.__class__.__name__

        print "UserInfo", id(base.UserInfo)
        if not base.UD.id:
            base.UD.id = 0

        if App.App.token == None:
            App.App.token = ""

        md.userId = base.UD.id
        print "send base" + App.App.token
        md.token = App.App.token
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

