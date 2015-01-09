#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import threading
import thread
import sys
import select
from time import sleep


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

    @classmethod
    def quit(cls):
         cls.is_quit = True

    def run(self):
            sys.stdout.write(">>"+"\n")
            sys.stdout.flush()
            while CommandInput.is_quit == False:
                sleep(.001)
                if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                    what = sys.stdin.readline()
                    what = what.replace('\n', '')
                    if what != "":
                        CommandInput.mutx.acquire()
                        CommandInput.queue.append(what)
                        CommandInput.mutx.release()

                    sys.stdout.write(">>"+"\n")
                    sys.stdout.flush()



        
