#!/usr/bin/env python

from Util import *
from Logger import *
import PBCommand_pb2

class S2CEquipInfo:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CEquipInfo()
        msg.ParseFromString(respByte)
        Logger.i("equip info back")
        for e in msg.equipList:
            Logger.i(e)
