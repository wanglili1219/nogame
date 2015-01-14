#!/usr/bin/python env
#-*- coding: utf-8 -*-

import threading
import thread
import sys
import time
import select

class CommandInput(threading.Thread):
    def __init__(self):
        self.isQuit = False
        super(CommandInput, self).__init__()
        self.mutx = threading.Lock()
        self.msgQueue = []

    def pop(self):
        if self.mutx.acquire(1):
            msg = ""
            if self.msgQueue:
                msg = self.msgQueue.pop(0)

            self.mutx.release()
            return msg

    def quit(self):
        self.isQuit = True

    def run(self):
        while not self.isQuit:
            if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                c = sys.stdin.readline()
                c = c.replace("\n", "")
                if self.mutx.acquire(1):
                    self.msgQueue.append(c)
                    self.mutx.release()
                    
            time.sleep(0.1)
            

            
