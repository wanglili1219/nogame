#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Util import *
import logging
import PBCommand_pb2
from S2CBase import *

class S2CPutOffEquip(S2CBase):
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CPutOffEquip()
        msg.ParseFromString(respByte)
        logging.info(str(msg.heroId))
        logging.info(str(msg.equipId))
