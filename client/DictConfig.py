import sys
import os
import os.path
from xdrlib import *
import xlrd

reload(sys)
sys.setdefaultencoding('utf-8')

Data = {}

def open_excel(file):
    try:
          data = xlrd.open_workbook(file)
          return data
    except Exception,e:
          print str(e)

def load_table(file):
    data = open_excel(file)
    table = data.sheets()[0]
    colname = table.row_values(1)
    coltype = table.row_values(2)
    row_map = {}
    for i in range(3, table.nrows - 1):
        row = table.row_values(i)
        row_map[row[0]] = {}
        for j in range(0, len(row) - 1):
            if colname[j] != "":
                row_map[row[0]][colname[j]] = row[j]

    return row_map

def init():
    for parent, dirnames, filenames in os.walk("./dict"): 
        for filename in filenames:
            ext = os.path.splitext(filename)[1][1:]
            basename = os.path.splitext(filename)[0]
            if ext == "xls":
                print "load", basename
                t = load_table(os.path.join(parent,filename))
                Data[basename] = t

