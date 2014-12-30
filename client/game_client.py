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

from Logger import *
from  CommandInput import *
from C2SLogin import *
from S2CLogin import *



serverHost = '127.0.0.1'    #default serverHost 
serverPort = 8084           #default serverPort
filename = 'hello.html'     #default filename
clientSocket = None

handlerDict = {}
outputs_set = []
            

def package_request(buf):
    return struct.pack('>i{0}s'.format(len(buf)), len(buf), buf)

def dispatch_message(respByte):
    md = PBApp_pb2.MsgDesc()
    md.ParseFromString(respByte)
    if md.errorCode != 0:
        Logger.e("respone error code " + str(md.errorCode) + "," + md.errorDesc)
        return

    inst = handlerDict[md.msgName]()
    inst.handle(md.msgBytes)

def gen_userinfo_request():
    global userId
    md = build_msgdes("C2SUserInfo")
    msg = PBApp_pb2.C2SUserInfo()
    msg.userId = userId
    md.msgBytes = msg.SerializeToString()
    
    return md.SerializeToString()
    
def handle_user_info(respByte):
    msg = PBApp_pb2.S2CUserInfo()
    msg.ParseFromString(respByte)
    Logger.i(msg.userId)
    Logger.i(msg.userName)

handlerDict["S2CLogin"] = globals()["S2CLogin"]
#handlerDict["S2CUserInfo"] = globals()[""]

try:
    clientSocket = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

Logger.init()
CommandInput.init()

while True:
    what = CommandInput.pop()
    
    sd = None
    if what == "login":
        l = C2SLogin()
        sd = package_request(l.build())
    elif what == "userinfo":
        sd = package_request(gen_userinfo_request())
    elif what == "quit":
        break

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
                    dispatch_message(body[0])
                
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
print("")
print("Bye Bye")

