package com.ease.nogame.gameserver;

import java.util.Date;

import org.hibernate.Session;

import com.ease.nogame.domain.Account;
import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.util.HibernateUtil;
import com.ease.nogame.util.IDGenerator;
import com.ease.nogame.util.TokenGenerator;
import com.google.protobuf.Message;

public class LoginHandler extends MessageHandler {
	@Override
	public void handle(Message msg){
		PBApp.C2SLogin req = (PBApp.C2SLogin)msg;
		Account acc = new Account();
		acc.setUserName(req.getUserName());
		acc.setPassword(req.getPassword());
		acc.setCreateTime(new Date());
		HibernateUtil.saveAndCommit(acc);

		PBApp.S2CLogin.Builder respb = PBApp.S2CLogin.newBuilder();
		respb.setUserId(IDGenerator.generate());
		respb.setToken(TokenGenerator.getToken());
		send(respb.build());
	}
}