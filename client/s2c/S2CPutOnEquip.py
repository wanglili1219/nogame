#!/usr/bin/env python

from Util import *
import logging
import PBCommand_pb2
from S2CBase import *

class S2CPutOnEquip(S2CBase):
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CPutOnEquip()
        msg.ParseFromString(respByte)
        logging.info(str(msg.hero))
