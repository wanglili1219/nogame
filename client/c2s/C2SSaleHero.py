#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
import PBCommand_pb2

class C2SSaleHero(C2SBase):
    def __init__(self, commandParam):
        self.heroId = commandParam["<heroId>"]

    def build(self):
        if not self.heroId or self.heroId == "":
            return ""
        
        msg = PBCommand_pb2.C2SSaleHero()
        msg.heroId = long(self.heroId)
        return self.wrapMsgDesc(msg)
