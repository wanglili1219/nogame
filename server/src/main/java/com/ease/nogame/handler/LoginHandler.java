package com.ease.nogame.handler;


import java.util.Date;
import java.io.UnsupportedEncodingException;

import org.hibernate.Session;

import com.ease.nogame.domain.Account;
import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.util.HibernateUtil;
import com.ease.nogame.util.IDGenerator;
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

		PBApp.S2CLogin.Builder resp = PBApp.S2CLogin.newBuilder();
		resp.setUserId(acc.getId());
		resp.setToken(acc.getToken());

		send(resp.build());
	}
}
