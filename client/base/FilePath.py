#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import os
import sys

class FilePath(object):
    def __init__(self):
        self.pwd = os.getcwd()
        self.searchPath = []

    def addSearchPath(self, path):
        print "addSearchPath " + path
        if path[0] == '/':
            if not os.path.exists(path):
                raise Exception(path + " not exist")
            self.searchPath.append(path)
        else:
            p = self.pwd + "/" + path
            if not os.path.exists(p):
                raise Exception(p + " not exist")
                
            print "append path " + p
            self.searchPath.append(p)
    
    def getFile(self, fileName):
        if fileName[0] != '/':
            fileName = '/' + fileName

        for p in self.searchPath:
            path = p + fileName
            print "iter :" + path
            if os.path.exists(path):
                return path
                
        raise Exception("Not found " + path)
    
