#!/usr/bin/env python

from Util import *
from Logger import *
import PBApp_pb2

class S2CHeroInfo:
    def handle(self, respByte):
        msg = PBApp_pb2.S2CHeroInfo()
        msg.ParseFromString(respByte)
        for h in msg.heroList:
            Logger.i(h)
