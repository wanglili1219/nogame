package com.ease.gameserver;

import io.netty.channel.ChannelHandlerContext;

import com.ease.protobuf.PBApp;


public class LoginHandler extends MessageHandler {
	@Override
	public void handle(ChannelHandlerContext ctx, Object msg){
		PBApp.C2SLogin req = (PBApp.C2SLogin)msg;
		System.out.println(req.getUserName());
		System.out.println(req.getPassword());
		System.out.println(req.getDeviceID());
		
		PBApp.S2CLogin.Builder respb = PBApp.S2CLogin.newBuilder();
		respb.setUserId("userid123456");
		respb.setToken("token123456");
		
		PBApp.MsgDesc.Builder mb = PBApp.MsgDesc.newBuilder();
		mb.setMsgName("S2Clogin");
		mb.setMsgBytes(respb.build().toByteString());
		
		ctx.writeAndFlush(mb.build());			
	}
}
