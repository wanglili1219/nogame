package com.ease.nogame.handler;

import org.hibernate.Session;

import com.ease.nogame.domain.Account;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class UserInfoHandler extends MessageHandler {

	@Override
	public void handle(Message msg) {
		Session s = HibernateUtil.currentSession();
		Account acc = (Account)s.get(Account.class, getUserId());

		PBMessage.PBUser.Builder pbu = PBMessage.PBUser.newBuilder();
		pbu.setUserId(acc.getId());
		pbu.setUserName(acc.getUserName());
		pbu.setLevel(acc.getLevel());
		pbu.setExp(acc.getExp());
		pbu.setGold(acc.getGold());
		pbu.setGem(acc.getGem());

		PBCommand.S2CUserInfo.Builder resp = PBCommand.S2CUserInfo.newBuilder();
		resp.setUserInfo(pbu.build());
		send(resp.build());
	}

}
