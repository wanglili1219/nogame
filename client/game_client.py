#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sys
import os
import socket
import string
import struct
import select
import threading
import thread
import re
import traceback
import time

apppath = os.getcwd()
sys.path.append(apppath + "./")
sys.path.append(apppath + "../common/")
sys.path.append(apppath + "/protoc/")
sys.path.append(apppath + "/c2s/")
sys.path.append(apppath + "/s2c/")
sys.path.append(apppath + "/resources/")
sys.path.append(apppath + "/core/")
sys.path.append(apppath + "/base/")

import App

if __name__ == "__main__":
    app = App.App()
    try:
        app.run()
    except:
        traceback.print_exc()
    finally:
        app.close()
        print("Bye Bye")

