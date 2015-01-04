#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Usage:
NGParamPaser.py login
NGParamPaser.py userinfo
NGParamPaser.py quit

"""
import sys 
from docopt import docopt, DocoptExit
from Logger import *

def parse(para):
    try:
        a = docopt(__doc__, argv=para)
    except DocoptExit as e:
        Logger.e("Invalid command!")
        return {}

    except SystemExit:
        return {}

    return a
