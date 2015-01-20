#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Usage:
NGParamPaser.py quit
NGParamPaser.py login
NGParamPaser.py userinfo
NGParamPaser.py heroinfo
NGParamPaser.py equipinfo
NGParamPaser.py puton <heroId> <equipId>
NGParamPaser.py putoff <heroId> <equipId>
NGParamPaser.py salehero <heroId>
"""
import sys 
import logging
from docopt import docopt, DocoptExit

def parse(para):
    try:
        a = docopt(__doc__, argv=para)
    except DocoptExit as e:
        logging.error("Invalid command!")
        logging.error(str(e))
        return {}

    except SystemExit:
        return {}

    return a
