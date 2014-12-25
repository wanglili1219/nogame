package com.ease.nogame.domain;

import java.util.Date;

public class Account {
	private String id;
	private String userName;
	private String password;
	private Date createTime;
	private Date accessTime;
	
	public void setId(String id){
		this.id = id;
	}
	
	public String getId(){
		return this.id;
	}
	
	public void setUserName(String name){
		this.userName = name;
	}
	
	public String getUserName(){
		return this.userName;
	}
	
	public void setPassword(String pass){
		this.password = pass;
	}
	
	public String getPassword(){
		return this.password;
	} 
	
	public void setCreateTime(Date t){
		this.createTime = t;
	}
	
	public Date getCreateTime(){
		return this.createTime;
	} 
	
	public void setAccessTime(Date t){
		this.accessTime = t;
	}
	
	public Date getAccessTime(){
		return this.accessTime;
	}
}
