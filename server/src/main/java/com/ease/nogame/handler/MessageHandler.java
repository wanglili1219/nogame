package com.ease.nogame.handler;

import com.ease.nogame.gameserver.NGException;
import com.ease.nogame.protobuf.PBMessage;
import com.google.protobuf.Message;

import io.netty.channel.ChannelHandlerContext;

public abstract class MessageHandler {
	private ChannelHandlerContext context = null;
	private long userId = 0;
	
	public MessageHandler() {

	}
	
	public abstract void handle(Message msg) throws NGException;
	
	public void transit(ChannelHandlerContext ctx, long userId, Message msg) throws NGException{
		this.context = ctx;
		this.userId = userId;
		handle(msg);
	}
	
	public void push(Message msg){
		//TODO
	}
	
	public long getUserId(){
		return this.userId;
	}

	public void send(Message msg){
		PBMessage.MsgDesc.Builder mb = PBMessage.MsgDesc.newBuilder();
		mb.setMsgName(msg.getClass().getSimpleName());
		mb.setMsgBytes(msg.toByteString());
		mb.setErrorCode(0);
		mb.setErrorDesc("OK");
		context.writeAndFlush(mb.build());
	}
}
