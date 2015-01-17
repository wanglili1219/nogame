#!/usr/bin/env python
#-*-coding utf-8 -*-

import unittest
import event

class TestEventHandler(event.BaseEventHandler):
    def handle(self, eventEntry):
        print "call handle inside TestEventHandler" + eventEntry.getName()
        
class TestBeRemoveHandler(event.BaseEventHandler):
    def handle(self, eventEntry):
        assert(False)

class TestEvent(event.BaseEvent):
    pass

class TestEventDispatcher(unittest.TestCase):
    def setUp(self):
        self.disp = event.EventDispatcher()
        pass

    def tearDown(self):
        pass

    def test_dispatch(self):
        self.disp.addEventHandler(TestEventHandler(event.EventDefine.TEST_FIRST_EVENT))
        self.disp.fire(TestEvent(event.EventDefine.TEST_FIRST_EVENT))
        self.disp.dispatch()

    def test_mutiple_dispatch(self):
        self.disp.addEventHandler(TestEventHandler(event.EventDefine.TEST_FIRST_EVENT))
        for i in range(5):
            self.disp.fire(TestEvent(event.EventDefine.TEST_FIRST_EVENT))
            self.disp.dispatch()

    def test_remove_handler(self):
        hdr = TestBeRemoveHandler(event.EventDefine.TEST_FIRST_EVENT)
        self.disp.addEventHandler(hdr)
        self.disp.fire(TestEvent(event.EventDefine.TEST_FIRST_EVENT))
        self.disp.removeEventHandler(hdr)
        self.disp.dispatch()
        
