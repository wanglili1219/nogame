package com.ease.gameserver;

import com.ease.protobuf.PBApp;
import com.google.protobuf.Message;

import io.netty.channel.ChannelHandlerContext;

public abstract class MessageHandler {
	private ChannelHandlerContext context = null;
	
	public MessageHandler() {

	}
	
	public abstract void handle(Message msg);
	
	public void transit(ChannelHandlerContext ctx, Message msg){
		context = ctx;
		handle(msg);
	}
	
	public void push(Message msg){
		//TODO
	}

	public void send(Message msg){
		System.out.println();
		PBApp.MsgDesc.Builder mb = PBApp.MsgDesc.newBuilder();
		mb.setMsgName(msg.getClass().getSimpleName());
		mb.setMsgBytes(msg.toByteString());
		context.writeAndFlush(mb.build());
	}
}
