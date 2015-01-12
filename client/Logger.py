#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import threading
import thread
import sys


class Logger(threading.Thread):
    def __init__(self):
        super(Logger, self).__init__()

        self.mutx = threading.Lock()
        self.queue = []
        self.is_quit = False

    def push(self, m):
        self.mutx.acquire()
        self.queue.append(m)
        self.mutx.release()

    def i(self, m):
        mm = str(m)
        self.push(mm)
    
    def e(self, m):
        mm = str(m)
        self.push(mm)
        
    def quit(self):
        self.is_quit = True

    def run(self):
        import time
        while self.is_quit == False:
            if self.mutx.acquire(1):
                for l in self.queue:
                    print(l)
                
                self.queue = []
                self.mutx.release()
            time.sleep(0.1)

sys.modules[__name__] = Logger()
