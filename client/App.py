#!/usr/bin/python env
#-*- coding: utf-8 -*-


import re
import time
import ConfigParser
import base
from base import *
import s2c
import event
import protoc

class App(object):
    def __init__(self):
        self.isQuit = False
        App.token = None

        base.FilePath.addSearchPath("./")
        base.FilePath.addSearchPath("resources/")

        base.CFG.read(base.FilePath.getFile("server.conf"))
        base.UserInfo.load()
        
        self.network = Network(App.network_handle)
        self.network.setDaemon(True)
        self.network.start()

        self.commandInput = CommandInput()
        self.commandInput.setDaemon(True)
        self.commandInput.start()
     
        Logger.setDaemon(True)
        Logger.start()

        Logger.i("Welcome...")
        Logger.i("userId: " + str(base.UD.id))
        Logger.i("userName: " + base.UD.name)
        Logger.i("userToken: " + base.UD.token)

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

print("local app")
