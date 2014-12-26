package com.ease.nogame.handler;

import org.hibernate.Session;

import com.ease.nogame.domain.Account;
import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class UserInfoHandler extends MessageHandler {

	@Override
	public void handle(Message msg) {
		PBApp.C2SUserInfo req = (PBApp.C2SUserInfo)msg;
		
		Session s = HibernateUtil.currentSession();
		Account acc = (Account)s.get(Account.class, req.getUserId());

		PBApp.S2CUserInfo.Builder resp = PBApp.S2CUserInfo.newBuilder();
		System.out.println(acc.getId());
		System.out.println(acc.getUserName());
		
		resp.setUserId(acc.getId());
		resp.setUserName(acc.getUserName());

		send(resp.build());
	}

}
