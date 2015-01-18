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

        App.FilePath = FilePath()
        App.FilePath.addSearchPath("./")
        App.FilePath.addSearchPath("resources/")

        App.CFG = ConfigParser.ConfigParser()
        App.CFG.read(App.FilePath.getFile("server.conf"))

        App.UserInfo = base.UserInfo()
        App.UserInfo.load()
        print App.UserInfo.id
        print "appid", id(App)

        self.network = Network(App.network_handle)
        self.network.setDaemon(True)
        self.network.start()

        self.commandInput = base.CommandInput()
        self.commandInput.setDaemon(True)
        self.commandInput.start()
     
        base.Logger.setDaemon(True)
        base.Logger.start()

        if App.UserInfo.token == None:
            Logger.i("Welcome for your first login.")
        else:
            Logger.i("Welcome come back.")
            Logger.i("userId: " + str(App.UserInfo.id))
            Logger.i("userName: " + App.UserInfo.name)
            Logger.i("userToken: " + App.UserInfo.token)

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
