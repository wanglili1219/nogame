#!/usr/bin/env python

from Util import *
import logging
import PBCommand_pb2

class S2CHeroInfo:
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CHeroInfo()
        msg.ParseFromString(respByte)
        for h in msg.heroList:
            logging.info(h)
