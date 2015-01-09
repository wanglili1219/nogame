#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import pickle
from Logger import *

class UserData:
    data = {} # data owner must be class

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

info = UserData()
