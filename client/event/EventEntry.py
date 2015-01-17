#!/usr/bin/python env
#-*-coding utf-8 -*-

class EventEntry(object):
    def __init__(self, name, context = None):
        self.name = name
        self.context = context

    def getName(self):
        return self.name

    def getContext(self):
        return self.context
