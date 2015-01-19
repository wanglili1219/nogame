#!/usr/bin/env python

from Util import *
import Logger
import PBCommand_pb2

class S2CEquipInfo:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CEquipInfo()
        msg.ParseFromString(respByte)
        print("equip info back")
        for e in msg.equipList:
            #Logger.i(e)
            print(e)
