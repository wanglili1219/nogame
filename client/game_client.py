#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys
import os
import socket
import string
import time
import struct
import select
import threading
import thread
import re
import traceback

apppath = os.getcwd()
sys.path.append(apppath + "./")
sys.path.append(apppath + "../common/")
sys.path.append(apppath + "/protoc/")
sys.path.append(apppath + "/c2s/")
sys.path.append(apppath + "/s2c/")

import PBMessage_pb2
import PBCommand_pb2

from C2SUserInfo import *
from S2CUserInfo import *
from Logger import *
from  CommandInput import *
from C2SLogin import *
from S2CLogin import *
import UserInfo
from C2SHeroInfo import *
import DictConfig
from C2SEquipInfo import *
from C2SPutOnEquip import *

import DispatchMessage
import NGParamPaser

serverHost = '127.0.0.1'    #default serverHost 
serverPort = 8084           #default serverPort
clientSocket = None

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
DispatchMessage.init()
DictConfig.init()
Logger.init()
CommandInput.init()
UserInfo.info.load()

if UserInfo.info.token == None:
    Logger.i("Welcome for your first login.")
else:
    Logger.i("Welcome come back.")
    Logger.i("userId: " + str(UserInfo.info.id))
    Logger.i("userName: " + UserInfo.info.name)
    Logger.i("userToken: " + UserInfo.info.token)

while True:
    paraList = {}
    what = ""
    what = CommandInput.pop()
    if what != "":
        paraList = NGParamPaser.parse(re.split("\s*", what))

    sd = None
    request = None
    try:
        if paraList["login"]:
            request = C2SLogin()
        elif paraList["userinfo"]:
            request = C2SUserInfo()
        elif paraList["heroinfo"]:
            request = C2SHeroInfo()
        elif paraList["equipinfo"]:
            request = C2SEquipInfo()
        elif paraList["wear"]:
            request = C2SPutOnEquip(paraList)
        elif paraList["quit"]:
            break
    except KeyError, e:
        pass

    if request != None and request != "":
        sd = package_request(request.build())
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
                    try:
                        DispatchMessage.dispatch(body[0])
                    except Exception, e:
                        traceback.print_exc()
                
        for w in writable:
            w.send(sd)
            sd = None
            outputs_set.remove(w)

    except Exception, e:
        traceback.print_exc()
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

