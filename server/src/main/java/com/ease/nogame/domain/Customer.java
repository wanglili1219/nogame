package com.ease.nogame.domain;

public class Customer {
	private int  	id;
	private int 	accountID;
	private String  address;
	
	public void setId(int id){
		this.id = id;
	}
	
	public int getId(){
		return this.id;
	}
	
	public void setAccountID(int id){
		this.accountID = id;
	}
	
	public int getAccountID(){
		return this.accountID;
	}
	
	public void setAddress(String addr){
		this.address = addr;
	}
	
	public String getAddress(){
		return this.address;
	}
}
