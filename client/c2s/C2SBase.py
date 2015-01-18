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

        print "UserInfo", id(base.UserInfo)
        if not base.UD.id:
            base.UD.id = 0

        if not base.UD.token:
           base.UD.token = ""

        md.userId = base.UD.id
        md.token = base.UD.token
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

