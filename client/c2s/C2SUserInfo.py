#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
import PBCommand_pb2

class C2SUserInfo(C2SBase):

    @C2SBase.check_login
    def build(self):
        msg = PBCommand_pb2.C2SUserInfo()
        return self.wrapMsgDesc(msg)

        
