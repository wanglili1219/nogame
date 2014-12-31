#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
from UserInfo import *
import PBApp_pb2

class C2SUserInfo(C2SBase):
    def build(self):
        msg = PBApp_pb2.C2SUserInfo()
        msg.userId = UserInfo.getId()
        return self.wrapMsgDesc(msg)

        
