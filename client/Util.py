#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import random
import uuid

def get_mac_address():
    mac = ""
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

def gen_user_name():
    tk = random.sample('abcdefghijklmnopqrstuvwyz0123456789', 5) 
    return "".join(tk)

