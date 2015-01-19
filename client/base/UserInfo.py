#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys
import pickle

class _Property(object):
    def __setattr__(self, k, v):
        self.__dict__[k] = v

    def __getattr__(self, k):
        if not k in self.__dict__:
            return None

        return self.__dict__[k]


property = _Property()

def load():
    global property
    try:
        fp = open("data.pkl", "rb")
        if fp:
            sd = pickle.load(fp)
            for k in sd:
                property.__dict__[k] = sd[k]

            fp.close()
    except Exception, e:
            print e

def dump():
    global property
    try:
        fp = open("data.pkl", "wb")
        if fp:
            sd = {}
            for k in property.__dict__:
                print k, property.__dict__[k]
                sd[k] = property.__dict__[k]
            
            pickle.dump(sd, fp)
            fp.close()
    except Exception, e:
            print e

def updateFromServerData(data):
    property.id    = data.userId
    property.name  = data.userName
    property.level = data.level
    property.exp   = data.exp
    property.gold  = data.gold
    property.gem   = data.gem
    dump()
