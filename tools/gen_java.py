#!/usr/bin/python
# -*- coding: utf-8 -*-

from Cheetah.Template import Template
import dict_java_class
import re
import string
import os
from xdrlib import *
import xlrd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def open_excel(file):
    try:
          data = xlrd.open_workbook(file)
          return data
    except Exception,e:
          print str(e)

def load_table(file):
    data = open_excel(file)
    table = data.sheets()[0]
    coldesc = table.row_values(0)
    colname = table.row_values(1)
    coltype = table.row_values(2)
    table_map = []
    for i in range(0, len(colname) - 1):
        if colname[i] != "":
            table_map.append([str(coldesc[i]), str(colname[i]), str(coltype[i])])
    
    return table_map

def init():
    dictpath = os.path.abspath('.') + "/../dict/"
    outpath = os.path.abspath('.') + "/java/"
    if not os.path.exists(outpath):
        os.mkdir(outpath)

    for parent, dirnames, filenames in os.walk(dictpath): 
        for filename in filenames:
            ext = os.path.splitext(filename)[1][1:]
            basename = os.path.splitext(filename)[0]
            tmpl = dict_java_class.dict_java_class()
            tmpl.className = basename
            if ext == "xls":
                path = os.path.join(parent,filename)
                print("load excel: " + path)
                t = load_table(path)
                tmpl.fieldList = t
                try:
                     fp = open(outpath + basename.capitalize() + ".java", "w+")
                     fp.write(str(tmpl))
                     fp.close()
                except Exception, e:
                    print "exception: ", e
                    

if __name__ == "__main__":
    init()
