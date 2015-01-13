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
import com.ease.nogame.handler.C2SEquipInfoHandler;
import com.ease.nogame.handler.C2SHeroInfoHandler;
import com.ease.nogame.handler.C2SLoginHandler;
import com.ease.nogame.handler.MessageHandler;
import com.ease.nogame.handler.C2SPutOnEquipHandler;
import com.ease.nogame.handler.C2SUserInfoHandler;
import com.ease.nogame.handler.C2SEquipInfoHandler;

import static com.ease.nogame.protobuf.PBMessage.*;
import static com.ease.nogame.protobuf.PBCommand.*;

import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.ByteString;
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
		
		public void handle(ChannelHandlerContext ctx, long userId, ByteString bs) 
				throws NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException , NGException{
			Method m = cMsg.getMethod("parseFrom", ByteString.class);
			((MessageHandler)cHandler.newInstance()).transit(ctx, userId, (Message)m.invoke(cMsg, bs));
		}
	}
	
	static void init(){
		try{
			Class<?>[] allcls = PBCommand.class.getClasses();
			for (Class<?> cls : allcls){
				String clsname = cls.getName();
				if (clsname.contains("OrBuilder") || clsname.contains("S2C")){
					continue;
				}

				handlerMap.put(cls.getSimpleName()
						, new HandlerEntry(Class.forName(cls.getName()),
							Class.forName("com.ease.nogame.handler." + cls.getSimpleName() + "Handler")));
			}
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
			System.exit(1);
		}
	}
	
	static void dispatch(ChannelHandlerContext ctx, Object msg) {
		MsgDesc md = (MsgDesc)msg;
		String loginname = C2SLogin.class.getSimpleName();
		System.out.println(md.getMsgName());
		System.out.println(md.getToken());
		if (md.getToken().isEmpty() && !md.getMsgName().equals(loginname)) {
			MsgDesc.Builder mb = MsgDesc.newBuilder();
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
						throw new NGException(NGErrorCode.INVALID_TOKEN);
					}
					
					if (md.getMsgName().equals(loginname)){
						throw new NGException(NGErrorCode.RELOGIN);
					}
				}

				HandlerEntry en = handlerMap.get(md.getMsgName());
				en.handle(ctx, md.getUserId(), md.getMsgBytes());
			}catch(NGException e){
				MsgDesc.Builder mb = MsgDesc.newBuilder();
				mb.setMsgName(md.getMsgName());
				mb.setErrorCode(e.getErrorCode());
				mb.setErrorDesc(e.getDesc());
				System.out.println("request error " + e.getDesc());
				ctx.writeAndFlush(mb.build());
			}catch(Exception e){
				e.printStackTrace();
				MsgDesc.Builder mb = MsgDesc.newBuilder();
				mb.setMsgName(md.getMsgName());
				mb.setErrorCode(2);
				mb.setErrorDesc("server inner error.");
				System.out.println("request error " + "server inner error.");
				ctx.writeAndFlush(mb.build());
			}
		}		
	}
}
