#!/usr/bin/python env
#-*- coding: utf-8 -*-

from C2SLogin import *
from C2SUserInfo import *
from C2SLogin import *
from C2SHeroInfo import *
from C2SEquipInfo import *
from C2SPutOnEquip import *
from C2SPutOffEquip import *
from C2SSaleHero import *

commandMap = {}
commandMap["login"]     = globals()["C2SLogin"]
commandMap["userinfo"]  = globals()["C2SUserInfo"]
commandMap["heroinfo"]  = globals()["C2SHeroInfo"]
commandMap["equipinfo"] = globals()["C2SEquipInfo"]
commandMap["puton"]     = globals()["C2SPutOnEquip"]
commandMap["putoff"]    = globals()["C2SPutOffEquip"]
commandMap["salehero"]  = globals()["C2SSaleHero"]

def handle(paraList):
    if not paraList:
        return False, None

    if paraList["quit"]:
        return True, None

    for k, v in enumerate(commandMap):
        if paraList[v]:
            return False, commandMap[v](paraList).build()
