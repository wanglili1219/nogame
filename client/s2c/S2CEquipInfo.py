#!/usr/bin/env python

from Util import *
import logging
import PBCommand_pb2

class S2CEquipInfo:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CEquipInfo()
        msg.ParseFromString(respByte)
        for e in msg.equipList:
            logging.info(e)
