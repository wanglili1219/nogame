package com.ease.nogame.domain;

import java.util.Date;

public class Account {
//	| id          | int(11) unsigned | NO   | PRI | NULL              | auto_increment              |
//| create_time | datetime         | NO   |     | NULL              |                             |
//| access_time | timestamp        | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
//| user_name   | varchar(128)     | NO   |     | NULL              |                             |
//| password    | varchar(128)     | NO   |     | NULL              |                             |
	
	private int id;
	private String userName;
	private String password;
	private Date createTime;
	private Date accessTime;
	
	public void setId(int id){
		this.id = id;
	}
	
	public int getId(){
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
