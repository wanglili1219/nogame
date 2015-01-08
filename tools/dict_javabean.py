#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
import string

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1420695896.333187
__CHEETAH_genTimestamp__ = 'Thu Jan  8 13:44:56 2015'
__CHEETAH_src__ = '/Users/user/work/workspace4.4/nogame/tools/dict_javabean.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jan  8 13:43:08 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class dict_javabean(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(dict_javabean, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def getCapName(self, name, **KWS):



        ## CHEETAH: generated from #def getCapName($name) at line 21, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        name = string.capwords(VFSL([locals()]+SL+[globals(), builtin],"name",True), sep="_").replace("_", "")
        return VFSL([locals()]+SL+[globals(), builtin],"name",True)
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def getFieldName(self, name, **KWS):



        ## CHEETAH: generated from #def getFieldName($name) at line 26, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        name = string.capwords(VFSL([locals()]+SL+[globals(), builtin],"name",True), sep="_").replace("_", "")
        name = VFN(VFSL([locals()]+SL+[globals(), builtin],"name",True)[0],"lower",False)() + VFSL([locals()]+SL+[globals(), builtin],"name",True)[1:]
        return VFSL([locals()]+SL+[globals(), builtin],"name",True)
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''package com.ease.nogame.dict;

import com.ease.nogame.gameserver.IDict;
import com.ease.nogame.util.Item;
import java.util.List;
import java.util.Map;

''')
        type_table = {        "int":"int",        "float":"float",        "string":"String",        "list<int>":"List<Integer>",        "list<item>":"List<Item>",        "list<string>":"List<String>",        "map":"Map<Integer, Integer>",        "double":"double",        "float":"float"    }
        write(u'''


''')
        clname = VFSL([locals()]+SL+[globals(), builtin],"getCapName",False)(VFSL([locals()]+SL+[globals(), builtin],"className",True))
        write(u'''public class DT''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"clname",True) # u'$clname' on line 33, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$clname')) # from line 33, col 16.
        write(u''' implements IDict {
''')
        for desc, name, type in VFSL([locals()]+SL+[globals(), builtin],"fieldList",True): # generated from line 34, col 5
            field_name = VFSL([locals()]+SL+[globals(), builtin],"getFieldName",False)(VFSL([locals()]+SL+[globals(), builtin],"name",True))
            write(u'''       //''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"desc",True) # u'$desc' on line 36, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'$desc')) # from line 36, col 10.
            write(u'''
       private ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"type_table",True)[str(VFSL([locals()]+SL+[globals(), builtin],"type",True))] # u'$type_table[str($type)]' on line 37, col 16
            if _v is not None: write(_filter(_v, rawExpr=u'$type_table[str($type)]')) # from line 37, col 16.
            write(u''' ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"field_name",True) # u'$field_name' on line 37, col 40
            if _v is not None: write(_filter(_v, rawExpr=u'$field_name')) # from line 37, col 40.
            write(u''';
''')
        write(u'''       
       @Override
       public Object getId() {
''')
        desc, name, type = VFSL([locals()]+SL+[globals(), builtin],"fieldList",True)[0]
        field_id_name = VFSL([locals()]+SL+[globals(), builtin],"getFieldName",False)(VFSL([locals()]+SL+[globals(), builtin],"name",True))
        write(u'''          return this.''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"field_id_name",True) # u'$field_id_name' on line 44, col 23
        if _v is not None: write(_filter(_v, rawExpr=u'$field_id_name')) # from line 44, col 23.
        write(u''';
       }

''')
        for desc, name, type in VFSL([locals()]+SL+[globals(), builtin],"fieldList",True): # generated from line 47, col 5
            method_name = VFSL([locals()]+SL+[globals(), builtin],"getCapName",False)(VFSL([locals()]+SL+[globals(), builtin],"name",True))
            field_name = VFSL([locals()]+SL+[globals(), builtin],"getFieldName",False)(VFSL([locals()]+SL+[globals(), builtin],"name",True))
            write(u'''       public ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"type_table",True)[str(VFSL([locals()]+SL+[globals(), builtin],"type",True))] # u'$type_table[str($type)]' on line 50, col 15
            if _v is not None: write(_filter(_v, rawExpr=u'$type_table[str($type)]')) # from line 50, col 15.
            write(u''' get''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"method_name",True) # u'${method_name}' on line 50, col 42
            if _v is not None: write(_filter(_v, rawExpr=u'${method_name}')) # from line 50, col 42.
            write(u'''(){
            return this.''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"field_name",True) # u'$field_name' on line 51, col 25
            if _v is not None: write(_filter(_v, rawExpr=u'$field_name')) # from line 51, col 25.
            write(u''';
       }

       public void set''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"method_name",True) # u'${method_name}' on line 54, col 23
            if _v is not None: write(_filter(_v, rawExpr=u'${method_name}')) # from line 54, col 23.
            write(u'''(''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"type_table",True)[str(VFSL([locals()]+SL+[globals(), builtin],"type",True))] # u'$type_table[str($type)]' on line 54, col 38
            if _v is not None: write(_filter(_v, rawExpr=u'$type_table[str($type)]')) # from line 54, col 38.
            write(u''' value){
            this.''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"field_name",True) # u'$field_name' on line 55, col 18
            if _v is not None: write(_filter(_v, rawExpr=u'$field_name')) # from line 55, col 18.
            write(u''' = value;
       }

''')
        write(u'''}

''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_dict_javabean= 'respond'

## END CLASS DEFINITION

if not hasattr(dict_javabean, '_initCheetahAttributes'):
    templateAPIClass = getattr(dict_javabean, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(dict_javabean)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=dict_javabean()).run()


