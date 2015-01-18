#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys
import pickle
import Logger 

class UserInfo(object):
    data = {} # data owner must be class

    def __setattr__(self, k, v):
        UserInfo.data[k] = v

    def __getattr__(self, k):
        print("__getattr__", k)
        if not k in UserInfo.data:
            return None
        return UserInfo.data[k]

    @staticmethod
    def dump():
        try:
            fp = open("data.pkl", "wb")
            if fp:
                pickle.dump(UserInfo.data, fp)
                fp.close()
        except Exception, e:
            print e

    @staticmethod
    def load():
        try:
            fp = open("data.pkl", "rb")
            if fp:
                UserInfo.data = pickle.load(fp)
                fp.close()
        except Exception, e:
            print e

    @staticmethod
    def updateFromServerData(data):
        UserInfo.data["id"]    = int(data.userId)
        UserInfo.data["name"]  = data.userName
        UserInfo.data["level"] = data.level
        UserInfo.data["exp"]  = data.exp
        UserInfo.data["gold"]  = data.gold
        UserInfo.data["gem"]   = data.gem
        print UserInfo.data
        UserInfo.dump()

