#!/usr/bin/env python
# -*- coding: utf-8 -*-  

class UserInfo:
    id = 0
    name = ""
    token = ""
    gold = ""

    @classmethod
    def setId(cls, id):
        cls.id = id
        
    @classmethod
    def getId(cls):
        return cls.id
    
    @classmethod
    def setName(cls, name):
        cls.name = name
    
    @classmethod
    def getName(cls):
        return cls.name
    
    @classmethod
    def setToken(cls, t):
        cls.token = t
    
    @classmethod
    def getToken(cls):
        return cls.token
