#!/usr/bin/env python
import sys
import socket
import string
import time
import struct
import select
import PBApp_pb2
import threading
import thread
import random
import uuid

serverHost = '127.0.0.1'    #default serverHost 
serverPort = 8084           #default serverPort
filename = 'hello.html'     #default filename
clientSocket = None

handlerDict = {}

#sockets from which we except to read

#sockets from which we expect to write
outputs_set = []

logQueue = []
cmdQueue = []

log_mutx = threading.Lock()
cmd_mutx = threading.Lock()

global isQuit
global token
global userId
isQuit = False
token = ""
userId = 0

def log(m):
    global logQueue
    log_mutx.acquire()
    logQueue.append(m)
    log_mutx.release()

def thr_eat_log(arg, arg2):
    global isQuit
    global logQueue
    while isQuit == False:
        log_mutx.acquire()
        for l in logQueue:
            print(l)

        logQueue = []
        log_mutx.release()
        time.sleep(0.1)

####################

def thr_command(arg1, arg2):
    while True:
        what = raw_input("what:")
        cmd_mutx.acquire()
        cmdQueue.append(what)
        cmd_mutx.release()
        time.sleep(0.1)

            

####################

def query_mac_address():
    mac = ""
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

def gen_user_name():
    tk = random.sample('abcdefghijklmnopqrstuvwyz0123456789', 5) 
    return "".join(tk)

def package_request(buf):
    return struct.pack('>i{0}s'.format(len(buf)), len(buf), buf)

def build_msgdes(msgName):
    global token
    global userId
    md = PBApp_pb2.MsgDesc()
    md.msgName = msgName
    md.token = token
    md.userId = userId
    return md
    
def gen_login_request():
    md = build_msgdes("C2SLogin")
    msg = PBApp_pb2.C2SLogin()
    msg.userName = gen_user_name()
    msg.password = "12345"
    msg.deviceID = query_mac_address()
    
    md.msgBytes = msg.SerializeToString()
    return md.SerializeToString()

def dispatch_message(respByte):
    md = PBApp_pb2.MsgDesc()
    md.ParseFromString(respByte)
    if md.errorCode != 0:
        log("response " + md.msgName + " " + md.errorDesc)
        return

    handlerDict[md.msgName](md.msgBytes)

def gen_userinfo_request():
    global userId
    md = build_msgdes("C2SUserInfo")
    msg = PBApp_pb2.C2SUserInfo()
    msg.userId = userId
    md.msgBytes = msg.SerializeToString()
    
    return md.SerializeToString()

def handle_login(respByte):
    global token
    global userId
    msg = PBApp_pb2.S2CLogin()
    msg.ParseFromString(respByte)
    token = msg.token
    userId = msg.userId
    log("handle_login " + token)
    
def handle_user_info(respByte):
    msg = PBApp_pb2.S2CUserInfo()
    msg.ParseFromString(respByte)
    log(msg.userId)
    log(msg.userName)

handlerDict["S2CLogin"] = handle_login
handlerDict["S2CUserInfo"] = handle_user_info

#run log thread
thread.start_new_thread(thr_eat_log, (1, 1))
thread.start_new_thread(thr_command, (1, 1))

try:
    clientSocket = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

clientSocket.connect((serverHost, serverPort))

while True:
    what = ""
    if cmd_mutx.acquire(1):
        if len(cmdQueue) > 0:
            what = cmdQueue[0]
            del cmdQueue[0]
       
        cmd_mutx.release()

    sd = None
    if what == "login":
        sd = package_request(gen_login_request())
    elif what == "userinfo":
        sd = package_request(gen_userinfo_request())
    elif what == "quit":
        break

    if sd != None:
        outputs_set.append(clientSocket)

    try: 
        readable, writable, exceptional = select.select([clientSocket], outputs_set, [clientSocket], 0)

        if exceptional:
            log("Connection exception.")
            clientSocket.close()
            clientSocket = None 
            self.sayHello = False
        
        for r in readable:
            headsize = 4
            headpacket = r.recv(headsize)
            if headpacket:
                if len(headpacket) == 0:
                    log("server break connect.")
                else:
                    bodysize = struct.unpack_from(">i", headpacket, 0)
                    bodypacket = r.recv(bodysize[0])
                    body = struct.unpack_from("%ds"%(bodysize), bodypacket, 0)
                    dispatch_message(body[0])
                
        for w in writable:
            w.send(sd)
            sd = None
            outputs_set.remove(w)

    except socket.error:
        clientSocket.close()
        clientSocket = None
    
    time.sleep(0.1)

clientSocket.close()
isQuit = True
print("")
print("bye")
