package com.ease.nogame.domain;

// Generated 2015-1-8 19:10:22 by Hibernate Tools 4.3.1

import java.util.Date;

/**
 * Account generated by hbm2java
 */
public class Account implements java.io.Serializable {

	private long id;
	private Date createTime;
	private Date accessTime;
	private String userName;
	private String password;
	private String token;
	private int gold;
	private int gem;
	private int level;
	private int exp;

	public Account() {
	}

	public Account(long id, Date createTime, Date accessTime, String userName,
			String password, int gold, int gem, int level, int exp) {
		this.id = id;
		this.createTime = createTime;
		this.accessTime = accessTime;
		this.userName = userName;
		this.password = password;
		this.gold = gold;
		this.gem = gem;
		this.level = level;
		this.exp = exp;
	}

	public Account(long id, Date createTime, Date accessTime, String userName,
			String password, String token, int gold, int gem, int level, int exp) {
		this.id = id;
		this.createTime = createTime;
		this.accessTime = accessTime;
		this.userName = userName;
		this.password = password;
		this.token = token;
		this.gold = gold;
		this.gem = gem;
		this.level = level;
		this.exp = exp;
	}

	public long getId() {
		return this.id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public Date getCreateTime() {
		return this.createTime;
	}

	public void setCreateTime(Date createTime) {
		this.createTime = createTime;
	}

	public Date getAccessTime() {
		return this.accessTime;
	}

	public void setAccessTime(Date accessTime) {
		this.accessTime = accessTime;
	}

	public String getUserName() {
		return this.userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return this.password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getToken() {
		return this.token;
	}

	public void setToken(String token) {
		this.token = token;
	}

	public int getGold() {
		return this.gold;
	}

	public void setGold(int gold) {
		this.gold = gold;
	}

	public int getGem() {
		return this.gem;
	}

	public void setGem(int gem) {
		this.gem = gem;
	}

	public int getLevel() {
		return this.level;
	}

	public void setLevel(int level) {
		this.level = level;
	}

	public int getExp() {
		return this.exp;
	}

	public void setExp(int exp) {
		this.exp = exp;
	}

}
