package com.ease.nogame.gameserver;

import java.util.Map.Entry;

import org.python.core.Py;
import org.python.core.PyDictionary;
import org.python.core.PyFunction;
import org.python.core.PyString;
import org.python.core.PySystemState;
import org.python.util.PythonInterpreter;

public class DictData {
	public static PyDictionary mData = null;
	public static void init(){
		if (mData != null){
			return;
		}
		
		String dictdir = System.getProperty("user.dir") + "/../common/DictConfig.py";
		PySystemState sys = Py.getSystemState();
		sys.path.add("/Library/Python/2.7/site-packages");
		PythonInterpreter interpreter = new PythonInterpreter();
		interpreter.execfile(dictdir);
	
		PyFunction func = (PyFunction) interpreter.get("init", PyFunction.class);
		mData =  (PyDictionary)func.__call__();
		interpreter.close();
		
//		for (Entry<PyObject, PyObject> entry : pd.getMap().entrySet()) {
//			System.out.println(entry.getKey().toString());
//            //            buf.append((entry.getValue()).__repr__().toString());
//        }
//		 
//		 PyString key = new PyString("hero");
//		 PyDictionary fileDict = (PyDictionary)pd.get(key);
//		 for (Entry<PyObject, PyObject> entry : fileDict.getMap().entrySet()){
//			 	System.out.println(entry.getKey().toString());
//		 }
		 
	}
	
	public static PyDictionary getExcelData(String fileName){
		if (mData == null){
			return null;
		}
		
		return (PyDictionary)mData.get(new PyString(fileName));
	}
}
