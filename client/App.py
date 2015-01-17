#!/usr/bin/python env
#-*- coding: utf-8 -*-


import re
import time
import UserInfo
import Logger
import DictConfig
import CommandHandler
from CommandInput import *
import s2c
import event
import NGParamPaser
from Network import *
import PBMessage_pb2
import PBCommand_pb2

import MessageDispatcher
from MessageDispatcher import *

class App(object):
    def __init__(self):
        self.isQuit = False

        self.network = Network(App.network_handle)
        self.network.setDaemon(True)
        self.network.start()

        self.commandInput = CommandInput()
        self.commandInput.setDaemon(True)
        self.commandInput.start()
        
        Logger.setDaemon(True)
        Logger.start()

        UserInfo.load()
        
        if UserInfo.token == None:
            Logger.i("Welcome for your first login.")
        else:
            Logger.i("Welcome come back.")
            Logger.i("userId: " + str(UserInfo.id))
            Logger.i("userName: " + UserInfo.name)
            Logger.i("userToken: " + UserInfo.token)

    @staticmethod
    def network_handle(data):
        MessageDispatcher.dispatch(data)

    def close(self):
        Logger.quit()
        self.commandInput.quit()
        self.network.quit()

    def run(self):
        event.EventDispatcher().fire(event.EventDefine.GAME_START)
        while True:
            paraList = None
            what = ""
            what = self.commandInput.pop()
            if what != "":
                paraList = NGParamPaser.parse(re.split("\s*", what))

            request = None
            self.isQuit, request = CommandHandler.handle(paraList)
            if self.isQuit:
                self.close()
                break

            if request != None and request != "":
                self.network.push(request)
            
            event.EventDispatcher().dispatch()

            time.sleep(0.1)

        event.EventDispatcher().fire(event.EventDefine.GAME_OVER)

