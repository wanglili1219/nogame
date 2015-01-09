#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import threading
import thread
import time
import sys

class Logger(threading.Thread):
    mutx = threading.Lock()
    queue = []
    is_quit = False
    inst = None
    
    @classmethod
    def push(cls, m):
        cls.mutx.acquire()
        cls.queue.append(m)
        cls.mutx.release()

    @classmethod
    def i(cls, m):
        mm = str(m)
        cls.push(mm)
    
    @classmethod
    def e(cls, m):
        mm = str(m)
        cls.push(mm)
        
    @classmethod
    def quit(cls):
        Logger.is_quit = True
        

    @classmethod
    def init(cls):
        i = Logger()
        i.start()
        Logger.inst = i

    def run(self):
        while Logger.is_quit == False:
            if Logger.mutx.acquire(1):
                for l in Logger.queue:
                    print(l)
                
                Logger.queue = []
                Logger.mutx.release()
            time.sleep(0.1)
