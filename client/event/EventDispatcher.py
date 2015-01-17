#!/usr/bin/env python
#-*-coding utf-8 -*-

from Singleton import *
from BaseEventHandler import *
from BaseEvent import *


class EventDispatcher(Singleton):
    def __init__(self):
        self.event_handler = {}
        self.fire_event = []
        self.remove_handler = []

    def addEventHandler(self, eventHandler):
        assert(isinstance(eventHandler, BaseEventHandler))
        
        evtname = eventHandler.getHandleEventName()
        if not self.event_handler.has_key(evtname):
            self.event_handler[evtname] = []

        self.event_handler[evtname].append(eventHandler)

    def fire(self, eventEntry):
        assert(isinstance(eventEntry, BaseEvent))
        self.fire_event.append(eventEntry)

    def removeEventHandler(self, handler):
        assert(isinstance(handler, BaseEventHandler))
        evtname = handler.getHandleEventName()

        if not self.event_handler.has_key(evtname):
            return

        self.remove_handler.append(handler)

    def dispatch(self):
        for hdr in self.remove_handler:
            evtname = hdr.getHandleEventName()
            if not self.event_handler.has_key(evtname):
                continue
            
            self.event_handler[evtname].remove(hdr)

        del self.remove_handler[:]

        for evtentry in self.fire_event:
            evtname = evtentry.getName()
            if not self.event_handler.has_key(evtname):
                continue

            for handler in self.event_handler[evtname]:
                handler.handle(evtentry)
        
        del self.fire_event[:]


