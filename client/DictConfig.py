import sys
import os
import os.path
from xdrlib import *
import xlrd
import DictConfig

reload(sys)
sys.setdefaultencoding('utf-8')

class dict_obj:
    pass

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
    table_map = {}
    for i in range(3, table.nrows - 1):
        row = table.row_values(i)
        obj = dict_obj()
        for j in range(0, len(row) - 1):
            if colname[j] != "":
                setattr(obj, colname[j], row[j])
        table_map[row[0]] = obj

    return table_map

def init():
    dictpath = os.path.abspath('.') + "/../dict/"
    for parent, dirnames, filenames in os.walk(dictpath): 
        for filename in filenames:
            ext = os.path.splitext(filename)[1][1:]
            basename = os.path.splitext(filename)[0]
            if ext == "xls":
                excelpath = os.path.join(parent,filename)
                print("load excel: " + excelpath)
                t = load_table(excelpath)
                DictConfig.__dict__[basename.upper()] = t
