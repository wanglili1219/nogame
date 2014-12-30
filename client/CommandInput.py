#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import threading
import thread
import time

class CommandInput(threading.Thread):
    mutx = threading.Lock()
    queue = []
    inst = None
    is_quit = False
    
    @classmethod
    def init(cls):
        inst = CommandInput()
        inst.start()
        CommandInput.inst = inst
    
    @classmethod
    def pop(cls):
        if cls.mutx.acquire(1):
            if len(cls.queue) > 0:
                what = cls.queue[0]
                del cls.queue[0]
                cls.mutx.release()
                return what
                
            cls.mutx.release()
            return ""

    def run(self):
        while CommandInput.is_quit == False:
            what = ""
            what = raw_input("what:")
            CommandInput.mutx.acquire()
            CommandInput.queue.append(what)
            CommandInput.mutx.release()
            time.sleep(0.1)
            if what == "quit":
                break


        
