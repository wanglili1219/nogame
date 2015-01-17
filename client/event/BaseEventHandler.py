#!/usr/bin/python env
#-*-coding utf-8 -*-

class BaseEventHandler(object):
    def __init__(self, evtName):
        self.name = evtName
    
    def handle(self, eventEntry):
        pass

    def getHandleEventName(self):
        return self.name
