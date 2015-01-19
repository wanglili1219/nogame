#!/usr/bin/env python

from Util import *
import base
import logging
import PBCommand_pb2
import event
import App

class S2CLogin:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CLogin()
        msg.ParseFromString(respByte)
        App.App.token = msg.token
        base.UserInfo.updateFromServerData(msg.userInfo)
        

        
