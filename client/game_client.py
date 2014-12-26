#!/usr/bin/env python
import sys
import socket
import string
import time
import struct
import PBApp_pb2

serverHost = '127.0.0.1'    #default serverHost 
serverPort = 8084           #default serverPort
filename = 'hello.html'     #default filename
clientSocket = None

handlerDict = {}



def gen_login_request():
    md = PBApp_pb2.MsgDesc()
    md.msgName = "C2SLogin"

    msg = PBApp_pb2.C2SLogin()
    msg.userName = "netease"
    msg.password = "12345"
    msg.deviceID = "98765431123abcdef"
    
    md.msgBytes = msg.SerializeToString()
    return md.SerializeToString()

def dispatch_message(respByte):
    md = PBApp_pb2.MsgDesc()
    md.ParseFromString(respByte)

    print(md.msgName)
    handlerDict[md.msgName](md.msgBytes)

    # msg = PBApp_pb2.S2CLogin()
    # msg.ParseFromString(md.msgBytes)
    # print(msg.userId)
    # print(msg.token)
    # print("====================")

def gen_userinfo_request():
    md = PBApp_pb2.MsgDesc()
    md.msgName = "C2SUserInfo"

    msg = PBApp_pb2.C2SUserInfo()
    msg.userId = "22015000201"
    md.msgBytes = msg.SerializeToString()
    return md.SerializeToString()

def handle_login(respByte):
    msg = PBApp_pb2.S2CLogin()
    msg.ParseFromString(respByte)
    print(msg.userId)
    print(msg.token)

def handle_user_info(respByte):
    msg = PBApp_pb2.S2CUserInfo()
    msg.ParseFromString(respByte)
    print(msg.userId)
    print(msg.userName)

handlerDict["S2CLogin"] = handle_login
handlerDict["S2CUserInfo"] = handle_user_info

try:
    clientSocket = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

clientSocket.connect((serverHost, serverPort))

while True:
    time.sleep(2)
    sd = gen_login_request()
    #sd = gen_userinfo_request()

    fmt = format
    data = struct.pack('>i{0}s'.format(len(sd)), len(sd), sd)
    clientSocket.sendall(data)  
    #clientSocket.sendall(sd)

    headsize = 4
    headpacket = clientSocket.recv(headsize)
    if headpacket:
        bodysize = struct.unpack_from(">i", headpacket, 0)
        print bodysize
        bodypacket = clientSocket.recv(bodysize[0])
        body = struct.unpack_from("%ds"%(bodysize), bodypacket, 0)
        print  "recv data:"
        dispatch_message(body[0])
 
#close socket to send eof to server
clientSocket.close()
