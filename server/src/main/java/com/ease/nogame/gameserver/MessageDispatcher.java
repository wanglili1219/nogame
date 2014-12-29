package com.ease.nogame.gameserver;


import io.netty.channel.ChannelHandlerContext;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.hibernate.Query;
import org.hibernate.Session;

import com.ease.nogame.domain.Account;
import com.ease.nogame.handler.LoginHandler;
import com.ease.nogame.handler.MessageHandler;
import com.ease.nogame.handler.UserInfoHandler;
import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.Message;


public class MessageDispatcher {
	public static Map<String, HandlerEntry> handlerMap = new HashMap<String, HandlerEntry>(); 
	
	public static class HandlerEntry{
		Class<?> cMsg = null;
		Class<?> cHandler = null;
		private HandlerEntry(Class<?> cMsg, Class<?> cHandler){
			this.cMsg = cMsg;
			this.cHandler = cHandler;
		}
		
		public void handle(ChannelHandlerContext ctx, ByteString bs) 
				throws NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException , NGException{
			Method m = cMsg.getMethod("parseFrom", ByteString.class);
			((MessageHandler)cHandler.newInstance()).transit(ctx, (Message)m.invoke(cMsg, bs));
		}
	}
	
	static void init(){
		handlerMap.put("C2SLogin", new HandlerEntry(PBApp.C2SLogin.class, LoginHandler.class));
		handlerMap.put("C2SUserInfo", new HandlerEntry(PBApp.C2SUserInfo.class, UserInfoHandler.class));

		//continue...
	}
	
	static void dispatch(ChannelHandlerContext ctx, Object msg) {
		PBApp.MsgDesc md = (PBApp.MsgDesc)msg;
		String loginname = PBApp.C2SLogin.class.getSimpleName();
		System.out.println(md.getMsgName());
		System.out.println(md.getToken());
		if (md.getToken().isEmpty() && !md.getMsgName().equals(loginname)) {
			PBApp.MsgDesc.Builder mb = PBApp.MsgDesc.newBuilder();
			mb.setMsgName("S2CLogin");
			mb.setErrorCode(1);
			mb.setErrorDesc("token null");
			ctx.writeAndFlush(mb.build());
		}else{
			try{
				String token = md.getToken();
				if (!token.isEmpty()){
					System.out.println("recv token " + token);
					Session s = HibernateUtil.currentSession();
					Query q = s.getNamedQuery("queryAccountByToken");
					System.out.println(q);
					q.setString("token", md.getToken());
//					if (q.getFetchSize() > 1 || q.getFetchSize() == 0) {
//						throw new NGException(1, "found multipy token in database.");
//					}

					List<Account> list = q.list();
					Account acc = (Account)list.get(0);
					if (!acc.getToken().equals(token) || !acc.getUserName().equals(acc.getUserName())){
						throw new NGException(1, "token error.");
					}
					
					if (md.getMsgName().equals(loginname)){
						throw new NGException(1, "relogin");
					}
				}

				HandlerEntry en = handlerMap.get(md.getMsgName());
				en.handle(ctx, md.getMsgBytes());
			}catch(NGException e){
				PBApp.MsgDesc.Builder mb = PBApp.MsgDesc.newBuilder();
				mb.setMsgName(md.getMsgName());
				mb.setErrorCode(e.getErrorCode());
				mb.setErrorDesc(e.getDesc());
				System.out.println("request error " + e.getDesc());
				ctx.writeAndFlush(mb.build());
			}catch(Exception e){
				e.printStackTrace();
				PBApp.MsgDesc.Builder mb = PBApp.MsgDesc.newBuilder();
				mb.setMsgName(md.getMsgName());
				mb.setErrorCode(2);
				mb.setErrorDesc("server inner error.");
				System.out.println("request error " + "server inner error.");
				ctx.writeAndFlush(mb.build());
			}
		}		
	}
}
