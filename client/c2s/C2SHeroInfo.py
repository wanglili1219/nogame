#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
import PBCommand_pb2

class C2SHeroInfo(C2SBase):
    def build(self):
        msg = PBCommand_pb2.C2SHeroInfo()
        return self.wrapMsgDesc(msg)
