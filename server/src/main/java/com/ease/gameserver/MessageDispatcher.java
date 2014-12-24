package com.ease.gameserver;


import io.netty.channel.ChannelHandlerContext;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

import com.ease.protobuf.PBApp;
import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.Message;
import com.google.protobuf.MessageLite;


public class MessageDispatcher {
	public static Map<String, HandlerEntry> handlerMap = new HashMap<String, HandlerEntry>(); 
	
	public static class HandlerEntry{
		Class<?> cMsg = null;
		Class<?> cHandler = null;
		private HandlerEntry(Class<?> cMsg, Class<?> cHandler){
			this.cMsg = cMsg;
			this.cHandler = cHandler;
		}
		
		public void handle(ChannelHandlerContext ctx, ByteString bs) throws NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException {
			Method m = cMsg.getMethod("parseFrom", ByteString.class);
			((MessageHandler)cHandler.newInstance()).transit(ctx, (Message)m.invoke(cMsg, bs));
		}
	}
	
	static void init(){
		handlerMap.put("C2SLogin", new HandlerEntry(PBApp.C2SLogin.class, LoginHandler.class));
		//continue...
		
	}
	
	static void dispatch(ChannelHandlerContext ctx, Object msg) throws ReflectiveOperationException, InvalidProtocolBufferException {
		PBApp.MsgDesc md = (PBApp.MsgDesc)msg;
		HandlerEntry en = handlerMap.get(md.getMsgName());
		en.handle(ctx, md.getMsgBytes());
	}
}
