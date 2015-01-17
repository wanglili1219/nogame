#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys
import pickle
import Logger 
import UserInfo
import event

class SaveUserInfo(event.BaseEventHandler):
    def handle(self, entry):
        print "SaveUserInfo from userData"

class UserData(object):
    data = {} # data owner must be class

    def __init__(self):
        event.EventDispatcher().addEventHandler(SaveUserInfo(event.EventDefine.USER_INFO_CHANGE))

    def __setattr__(self, k, v):
        UserData.data[k] = v

    def __getattr__(self, k):
        if not UserData.data.has_key(k):
            return None
        return UserData.data[k]

    def dump(self):
        path = "data.pkl"
        try:
            fp = open(path, "wb")
            if fp:
                pickle.dump(UserData.data, fp)
                fp.close()
        except Exception, e:
            print e

    def load(self):
        path = "data.pkl"
        try:
            fp = open(path, "rb")
            if fp:
                UserData.data = pickle.load(fp)
                fp.close()
        except Exception, e:
            print e

sys.modules[__name__] = UserData()
