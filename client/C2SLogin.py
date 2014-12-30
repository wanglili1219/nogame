#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
from Util import *

class C2SLogin(C2SBase):
    def build(self):
        msg = PBApp_pb2.C2SLogin()
        msg.userName = Util.gen_user_name()
        msg.password = "12345"
        msg.deviceID = Util.get_mac_address()
        return self.wrapMsgDesc("C2SLogin", msg)

        
        
