#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys
import pickle
import Logger 

class UserInfo(object):
    data = {} # data owner must be class

    def __init__(self):
        self.dataFile = "data.pkl"
        
    def __setattr__(self, k, v):
        UserInfo.data[k] = v

    def __getattr__(self, k):
        print("__getattr__", k)
        if not k in UserInfo.data:
            return None
        return UserInfo.data[k]

    def dump(self):
        try:
            fp = open(self.dataFile, "wb")
            if fp:
                pickle.dump(UserInfo.data, fp)
                fp.close()
        except Exception, e:
            print e

    def load(self):
        try:
            fp = open(self.dataFile, "rb")
            if fp:
                UserInfo.data = pickle.load(fp)
                fp.close()
        except Exception, e:
            print e

    def updateFromServerData(self, data):
        UserInfo.data.id    = data.userId
        UserInfo.data.name  = data.userName
        UserInfo.data.level = data.level
        UserInfo.data.exp   = data.exp
        UserInfo.data.gold  = data.gold
        UserInfo.data.gem   = data.gem
        self.dump()

