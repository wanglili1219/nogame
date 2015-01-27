#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import PBMessage_pb2
import base
import App
import logging

class C2SBase(object):
    def __init__(self, commandParam):
        self.commandParam = commandParam

    @staticmethod
    def check_login(func):
        def wrap(self):
            if App.App.token == None and self.commandParam["login"] == False:
                raise Exception("No login.")

            r = func(self)
            return r
        return wrap
    
    def wrapMsgDesc(self, msg):
        md = PBMessage_pb2.MsgDesc()
        md.msgName = msg.__class__.__name__

        if not base.UserInfo.property.id:
            base.UserInfo.property.id = 0

        if App.App.token == None:
            App.App.token = ""

        md.userId = base.UserInfo.property.id
        md.token = App.App.token
        md.msgBytes = msg.SerializeToString()
        return md.SerializeToString()

        

