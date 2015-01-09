#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
import PBCommand_pb2

class C2SEquipInfo(C2SBase):
    def build(self):
        msg = PBCommand_pb2.C2SEquipInfo()
        return self.wrapMsgDesc(msg)
