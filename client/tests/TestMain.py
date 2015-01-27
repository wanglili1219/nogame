#!/usr/bin/env python
#-*-coding utf-8 -*-

import os
import sys
import unittest

apppath = os.getcwd()
sys.path.append(apppath + "/../")

from testEventDispatcher import *


if __name__ == "__main__":
    unittest.main()

