#!/usr/bin/env python
# -*- coding: utf-8 -*-  



import sys
import socket
import string
import time
import struct
import select
import PBApp_pb2
import threading
import thread
import re

sys.path.append("../common/")

from C2SUserInfo import *
from S2CUserInfo import *
from Logger import *
from  CommandInput import *
from C2SLogin import *
from S2CLogin import *
from UserInfo import *
import DictConfig

import DispatchMessage
import NGParamPaser

serverHost = '127.0.0.1'    #default serverHost 
serverPort = 8084           #default serverPort
clientSocket = None

handlerDict = {}
outputs_set = []
            

def package_request(buf):
    return struct.pack('>i{0}s'.format(len(buf)), len(buf), buf)

try:
    clientSocket = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

#
#init
#
DictConfig.init()
Logger.init()
CommandInput.init()
UserInfo.load()

if UserInfo.getToken() == "":
    Logger.i("Welcome for your first login.")
else:
    Logger.i("Welcome come back.")
    Logger.i("userId: " + str(UserInfo.getId()))
    Logger.i("userName: " + UserInfo.getName())
    Logger.i("userToken: " + UserInfo.getToken())

while True:
    paraList = {}
    what = ""
    what = CommandInput.pop()
    if what != "":
        paraList = NGParamPaser.parse(re.split("\s*", what))

    sd = None
    try:
        if paraList["login"]:
            l = C2SLogin()
            sd = package_request(l.build())
        elif paraList["userinfo"]:
            l = C2SUserInfo()
            sd = package_request(l.build())
        elif paraList["quit"]:
            break
    except KeyError, e:
        pass

    if sd != None:
        outputs_set.append(clientSocket)

    try: 
        readable, writable, exceptional = select.select([clientSocket], outputs_set, [clientSocket], 0)

        if exceptional:
            Logger.i("Connection exception.")
            clientSocket.close()
            clientSocket = None 
            self.sayHello = False
        
        for r in readable:
            headsize = 4
            headpacket = r.recv(headsize)
            if headpacket:
                if len(headpacket) == 0:
                    Logger.i("server break connect.")
                else:
                    bodysize = struct.unpack_from(">i", headpacket, 0)
                    bodypacket = r.recv(bodysize[0])
                    body = struct.unpack_from("%ds"%(bodysize), bodypacket, 0)
                    DispatchMessage.dispatch(body[0])
                
        for w in writable:
            w.send(sd)
            sd = None
            outputs_set.remove(w)

    except Exception, e:
        print e
        clientSocket.close()
        clientSocket = None
        break
    
    time.sleep(0.1)

if clientSocket != None:
    clientSocket.close()

Logger.quit()
CommandInput.quit()

print("")
print("Bye Bye")

