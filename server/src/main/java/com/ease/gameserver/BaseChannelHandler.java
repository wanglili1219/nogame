package com.ease.gameserver;

import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

public class BaseChannelHandler extends ChannelInboundHandlerAdapter{
	@Override
	public void channelActive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("client connect " + ctx.channel().remoteAddress());
        ctx.fireChannelActive();
    }

    @Override
    public void channelInactive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("client break connector " + ctx.channel().remoteAddress());
        ctx.fireChannelInactive();
    }
	
    @Override
	public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
		MessageDispatcher.dispatch(ctx, msg);
		ctx.fireChannelRead(msg);
	}
 		  
	@Override
	public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
		cause.printStackTrace();
		ctx.close();
	}
}

