#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
import Util
import PBCommand_pb2

class C2SLogin(C2SBase):
    def build(self):
        msg = PBCommand_pb2.C2SLogin()
        msg.userName = Util.gen_user_name()
        msg.password = "12345"
        msg.deviceID = Util.get_mac_address()
        ss = self.wrapMsgDesc(msg)
        return ss

        
        
