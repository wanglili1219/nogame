#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import Network
import sys
import os
import socket
import string
import struct
import select
import threading
import thread
import traceback
import time

serverHost = '127.0.0.1'    
serverPort = 8084

class Network(threading.Thread):
    def __init__(self, handler):
        super(Network, self).__init__()
        
        self.handler = handler
        self.isQuit = False
        self.mutx = threading.Lock()
        self.clientSocket = None
        self.msgQueue = []
        self.outputs_set = []

        try:
            self.clientSocket = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((serverHost, serverPort))
        except socket.error, msg:
            logging.error('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
            sys.exit();

    def quit(self):
        self.isQuit = True
        
    def __package_message(self, buf):
        return struct.pack('>i{0}s'.format(len(buf)), len(buf), buf)

    def init(self):
        if not self.isAlive():
            self.start()

    def push(self, msg):
        self.mutx.acquire()
        self.msgQueue.append(msg)
        if not self.clientSocket in self.outputs_set:
            self.outputs_set.append(self.clientSocket)
        self.mutx.release()

    def run(self):
        while not self.isQuit:
            readable, writable, exceptional = select.select([self.clientSocket], self.outputs_set, [self.clientSocket], 0)
            if exceptional:
                self.clientSocket.close()
                clientSocket = None 
            
            for r in readable:
                headsize = 4
                headpacket = r.recv(headsize)
                if headpacket:
                    if len(headpacket) == 0:
                        logging.info("server break connect.")
                    else:
                        bodysize = struct.unpack_from(">i", headpacket, 0)
                        bodypacket = r.recv(bodysize[0])
                        body = struct.unpack_from("%ds"%(bodysize), bodypacket, 0)
                        try:
                            if self.handler: 
                                self.handler(body[0])
                        except Exception, e:
                            traceback.print_exc()
                        
            for w in writable:
                if self.mutx.acquire(1):
                    for m in self.msgQueue:
                        buf = self.__package_message(m)
                        w.send(buf)
                    self.mutx.release()
                self.outputs_set.remove(w)

            time.sleep(0.1)
        
        if self.clientSocket:
            self.clientSocket.close()
            self.clientSocket = None
