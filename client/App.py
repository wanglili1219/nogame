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
import logging

class App(object):
    def __init__(self):
        self.isQuit = False
        App.token = None
        
        logging.basicConfig(level=logging.DEBUG, format='%(filename)s:%(lineno)d %(levelname)s %(message)s')
        base.FilePath.addSearchPath("./")
        base.FilePath.addSearchPath("resources/")

        base.CFG.read(base.FilePath.getFile("server.conf"))
        
        self.network = Network(App.network_handle)
        self.network.setDaemon(True)
        self.network.start()

        self.commandInput = CommandInput()
        self.commandInput.setDaemon(True)
        self.commandInput.start()
     
        base.UserInfo.load()
        logging.info("Welcome for you come.")
        logging.info("userId: " + str(base.UserInfo.property.id))
        logging.info("userName: " + base.UserInfo.property.name)
        logging.info("userToken: " + base.UserInfo.property.token)

    @staticmethod
    def network_handle(data):
        MessageDispatcher.dispatch(data)

    def close(self):
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

