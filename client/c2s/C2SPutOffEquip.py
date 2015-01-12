#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from C2SBase import *
import PBCommand_pb2
import Logger

class C2SPutOffEquip(C2SBase):
    def __init__(self, commandParam):
        self.heroId = commandParam["<heroId>"]
        self.equipId = commandParam["<equipId>"]

    def build(self):
        if not self.heroId or not self.equipId:
            return ""

        msg = PBCommand_pb2.C2SPutOffEquip()
        msg.heroId = long(self.heroId)
        msg.equipId = long(self.equipId)
        return self.wrapMsgDesc(msg)
