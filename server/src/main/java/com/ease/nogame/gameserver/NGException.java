package com.ease.nogame.gameserver;

public class NGException extends Exception {
	private int code;
	private String desc;
	
	public NGException(int code, String desc){
		super(desc);
		this.code = code;
		this.desc = desc;
	}
	
	public int getErrorCode(){
		return code;
	}
	
	public String getDesc(){
		return desc;
	}
}
