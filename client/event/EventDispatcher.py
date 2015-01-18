#!/usr/bin/env python
#-*-coding utf-8 -*-

from Singleton import *
from BaseEventHandler import *
from EventEntry import *


class EventDispatcher(Singleton):
    __event_handler  = {}
    __fire_event     = []
    __remove_handler = []

    def addEventHandler(self, eventHandler):
        assert(isinstance(eventHandler, BaseEventHandler))
        
        evtname = eventHandler.getHandleEventName()
        if not evtname in self.__event_handler:
            self.__event_handler[evtname] = []

        self.__event_handler[evtname].append(eventHandler)

    def fire(self, eventName, context = None):
        assert(isinstance(eventName, basestring))
        context = {} if context == None else context
        entry = EventEntry(eventName, context)
        self.__fire_event.append(entry)

    def removeEventHandler(self, handler):
        assert(isinstance(handler, BaseEventHandler))
        evtname = handler.getHandleEventName()

        if not evtname in self.__event_handler:
            return

        self.__remove_handler.append(handler)

    def dispatch(self):
        for hdr in self.__remove_handler:
            evtname = hdr.getHandleEventName()
            if not evtname in self.__event_handler:
                continue
            
            self.__event_handler[evtname].remove(hdr)

        del self.__remove_handler[:]

        for evtentry in self.__fire_event:
            evtname = evtentry.getName()
            if not evtname in self.__event_handler:
                continue

            for handler in self.__event_handler[evtname]:
                handler.handle(evtentry)
        
        del self.__fire_event[:]


