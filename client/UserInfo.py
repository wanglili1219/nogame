#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import pickle
from Logger import *

class UserInfo:
    data = {
        "id":"0",
        "name":"",
        "token":"",
        "gold":"",
    }

    @classmethod
    def setId(cls, id):
        UserInfo.data["id"] = id
        
    @classmethod
    def getId(cls):
        return UserInfo.data["id"]
    
    @classmethod
    def setName(cls, n):
        cls.data["name"] = n
    
    @classmethod
    def getName(cls):
        return cls.data["name"]
    
    @classmethod
    def setToken(cls, t):
        cls.data["token"] = t
    
    @classmethod
    def getToken(cls):
        return cls.data["token"]

    @classmethod
    def dump(cls):
        path = "data.pkl"
        try:
            fp = open(path, "wb")
            if fp:
                Logger.i("dump userinfo")
                pickle.dump(cls.data, fp)
                fp.close()
        except Exception, e:
            print e

    @classmethod
    def load(cls):
        path = "data.pkl"
        try:
            fp = open(path, "rb")
            if fp:
                cls.data = pickle.load(fp)
                fp.close()
        except Exception, e:
            print e
