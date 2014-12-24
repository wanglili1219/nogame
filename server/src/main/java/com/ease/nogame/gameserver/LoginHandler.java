package com.ease.nogame.gameserver;

import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.util.IDGenerator;
import com.ease.nogame.util.TokenGenerator;
import com.google.protobuf.Message;

public class LoginHandler extends MessageHandler {
	@Override
	public void handle(Message msg){
		PBApp.C2SLogin req = (PBApp.C2SLogin)msg;
		System.out.println(req.getUserName());
		System.out.println(req.getPassword());
		System.out.println(req.getDeviceID());

		PBApp.S2CLogin.Builder respb = PBApp.S2CLogin.newBuilder();
		respb.setUserId(IDGenerator.generate());
		respb.setToken(TokenGenerator.getToken());
		send(respb.build());
	}
}
