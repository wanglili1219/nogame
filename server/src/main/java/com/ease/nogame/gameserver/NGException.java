package com.ease.nogame.gameserver;

public class NGException extends Exception {
	private int code;
	private String desc;
	
	public NGException(int code, String desc){
		super(desc);
		this.code = code;
		this.desc = desc;
	}
	
	public NGException(NGErrorCode ec, Object...args){
		this.code = ec.code;
		this.desc = ec.desc;
		for (Object obj : args){
			this.desc = this.desc + "," + String.valueOf(obj);
		}
	}
	
	public int getErrorCode(){
		return this.code;
	}
	
	public String getDesc(){
		return this.desc;
	}
}
