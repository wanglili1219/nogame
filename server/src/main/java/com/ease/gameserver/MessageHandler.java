package com.ease.gameserver;

import io.netty.channel.ChannelHandlerContext;

public abstract class MessageHandler {
	public MessageHandler() {

	}
	
	public abstract void handle(ChannelHandlerContext ctx, Object msg);
}
