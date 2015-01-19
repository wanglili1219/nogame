#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Util import *
import logging
import PBCommand_pb2
from S2CBase import *

class S2CSaleHero(S2CBase):
    def handle(self, respByte):
        msg = PBCommand_pb2.S2CSaleHero()
        msg.ParseFromString(respByte)
        logging.info(str(msg.heroId))
        logging.info(str(msg.saleGold))
