#!/usr/bin/python env
#-*- coding: utf-8 -*-


import re
import UserInfo
import Logger
import DictConfig
import CommandHandler
from CommandInput import *
from S2CLogin import *
import NGParamPaser
from Network import *
import PBMessage_pb2
import PBCommand_pb2

class App(object):
    def __init__(self):
        self.isQuit = False

        self.network = Network()
        self.network.setDaemon(True)
        self.network.start()

        DictConfig.init()
        Logger.setDaemon(True)
        Logger.start()

        CommandInput.init()
        UserInfo.load()

        if UserInfo.token == None:
            Logger.i("Welcome for your first login.")
        else:
            Logger.i("Welcome come back.")
            Logger.i("userId: " + str(UserInfo.id))
            Logger.i("userName: " + UserInfo.name)
            Logger.i("userToken: " + UserInfo.token)

    def close(self):
        Logger.quit()
        CommandInput.quit()
        self.network.quit()

    def run(self):
        while True:
            paraList = {}
            what = ""
            what = CommandInput.pop()
            if what != "":
                paraList = NGParamPaser.parse(re.split("\s*", what))

            request = None
            self.isQuit, request = CommandHandler.handle(paraList)
            if self.isQuit:
                self.close()
                break

            if request != None and request != "":
                self.network.push(request)

