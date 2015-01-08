package com.ease.nogame.handler;


import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.io.UnsupportedEncodingException;

import org.hibernate.Session;

import com.ease.nogame.dict.DTManager;
import com.ease.nogame.dict.DTPlayerInitial;
import com.ease.nogame.domain.Account;
import com.ease.nogame.domain.Hero;
import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.util.HibernateUtil;
import com.ease.nogame.util.IDGenerator;
import com.ease.nogame.util.Item;
import com.ease.nogame.util.TokenGenerator;
import com.google.protobuf.Message;

public class LoginHandler extends MessageHandler {
	@Override
	public void handle(Message msg) {
		PBApp.C2SLogin req = (PBApp.C2SLogin)msg;

		Account acc = new Account();
		acc.setUserName(req.getUserName());
		acc.setPassword(req.getPassword());
		acc.setCreateTime(new Date());
		acc.setToken(TokenGenerator.getToken());
		HibernateUtil.saveAndCommit(acc);
		
		DTPlayerInitial dtpi = DTManager.PLAYER_INITIAL.getByID(1);
		List<Item> itmlst = dtpi.getInitialItem();
		List<Object> savelst = new ArrayList<Object>();
		for (Item itm : itmlst){
			if (itm.getType() ==  25){
				Hero h = new Hero();
				h.setAccountId(acc.getId());
				h.setDictId(itm.getId());
				h.setLevel(1);
				h.setExp(0);
				savelst.add(h);
			}
		}
		
		HibernateUtil.saveObjectsAndCommit(savelst);

		PBApp.S2CLogin.Builder resp = PBApp.S2CLogin.newBuilder();
		resp.setUserId(acc.getId());
		resp.setToken(acc.getToken());

		send(resp.build());
	}
}
