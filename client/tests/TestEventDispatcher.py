#!/usr/bin/env python
#-*-coding utf-8 -*-

import unittest
import event

class TestEventHandler(event.BaseEventHandler):
    def handle(self, eventEntry):
        print "call handle " + eventEntry.getName()
        
class TestBeRemoveHandler(event.BaseEventHandler):
    def handle(self, eventEntry):
        assert(False)

class HasContextHandler(event.BaseEventHandler):
    def handle(self, eventEntry):
        assert(eventEntry.getContext()["fruit"] is "apple")
        

class TestEventDispatcher(unittest.TestCase):
    def setUp(self):
        self.disp = event.EventDispatcher()
        pass

    def tearDown(self):
        pass

    def test_dispatch(self):
        hdr = TestEventHandler(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.addEventHandler(hdr)
        self.disp.fire(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.dispatch()
        self.disp.removeEventHandler(hdr)

    def test_mutiple_dispatch(self):
        hdr = TestEventHandler(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.addEventHandler(hdr)
        for i in range(5):
            self.disp.fire(event.EventDefine.TEST_FIRST_EVENT)
            self.disp.dispatch()

        self.disp.removeEventHandler(hdr)

    def test_remove_handler(self):
        hdr = TestBeRemoveHandler(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.addEventHandler(hdr)
        self.disp.fire(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.removeEventHandler(hdr)
        self.disp.dispatch()
        
    def test_context(self):
        hdr = HasContextHandler(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.addEventHandler(hdr)
        self.disp.fire(event.EventDefine.TEST_FIRST_EVENT, {"fruit":"apple"})
        self.disp.dispatch()
        self.disp.removeEventHandler(hdr)
        
