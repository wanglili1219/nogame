package com.ease.nogame.gameserver;


public enum NGErrorCode {
	NOT_FOUND_DICT_ID, 
	INVALID_TOKEN,
	RELOGIN,
	NOT_FOUND_HERO,
	NOT_FOUND_HERO_CONFIG,
	NOT_FOUND_EQUIP,
	HERO_NOT_HAS_EQUIP,
	HERO_ALREADY_ATTACH_EQUIP,
	;
	
	//to continue...
	public int code = 0;
	public String desc = "NO DESC";
		
	private NGErrorCode() {
		this.code = Const.BASE_ERROR_CODE + this.ordinal();
		this.desc = this.toString().replaceAll("_", " ");
	}
}
