#!/usr/bin/env python

from Util import *
import base
import Logger
import PBCommand_pb2
import event
import App

class S2CLogin:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CLogin()
        msg.ParseFromString(respByte)
        App.App.token = msg.token
        print "app token", App.App.token
        base.UserInfo.updateFromServerData(msg.userInfo)
        

        
