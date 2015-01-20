#!/usr/bin/python env
#-*- coding: utf-8 -*-

import threading
import thread
import sys
import time
import select
import Queue

class CommandInput(threading.Thread):
    def __init__(self):
        self.isQuit = False
        super(CommandInput, self).__init__()
        self.msgQueue = Queue.Queue()

    def pop(self):
            msg = ""
            if not self.msgQueue.empty():
                msg = self.msgQueue.get()

            return msg

    def quit(self):
        self.isQuit = True

    def run(self):
        while not self.isQuit:
            if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                c = sys.stdin.readline()
                c = c.replace("\n", "")
                self.msgQueue.put(c)
                    
            time.sleep(0.1)
            

            
