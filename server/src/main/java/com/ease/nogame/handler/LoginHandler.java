package com.ease.nogame.handler;


import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.io.UnsupportedEncodingException;

import org.hibernate.Session;

import com.ease.nogame.dict.DTEquip;
import com.ease.nogame.dict.DTManager;
import com.ease.nogame.dict.DTPlayerInitial;
import com.ease.nogame.domain.Account;
import com.ease.nogame.domain.Equip;
import com.ease.nogame.domain.Hero;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.util.HibernateUtil;
import com.ease.nogame.util.IDGenerator;
import com.ease.nogame.util.Item;
import com.ease.nogame.util.TokenGenerator;
import com.google.protobuf.Message;

public class LoginHandler extends MessageHandler {
	@Override
	public void handle(Message msg) {
		PBCommand.C2SLogin req = (PBCommand.C2SLogin)msg;

		Account acc = new Account();
		acc.setUserName(req.getUserName());
		acc.setPassword(req.getPassword());
		acc.setCreateTime(new Date());
		acc.setToken(TokenGenerator.getToken());

		///add hero
		DTPlayerInitial dtpi = DTManager.PLAYER_INITIAL.getByID(1);
		acc.setLevel(dtpi.getPlayerInitialLv());
		acc.setExp(dtpi.getPlayerInitialExp());
		acc.setGold(dtpi.getPlayerInitialGold());
		acc.setGem(dtpi.getPlayerInitialDiamond());
		HibernateUtil.saveAndCommit(acc);

		List<Item> itmlst = dtpi.getInitialItem();
		List<Object> savelst = new ArrayList<Object>();
		for (Item itm : itmlst){
			if (itm.getType() ==  25){
				Hero h = new Hero();
				h.setDictId(itm.getId());
				h.setLevel(1);
				h.setExp(0);
				h.setUserId(acc.getId());
				savelst.add(h);
			}
		}
		
		HibernateUtil.saveObjectsAndCommit(savelst);

		///add equip
		List<DTEquip> eqlst = DTManager.EQUIP.getList();
		List<Object> saveeqlst = new ArrayList<Object>();
		int eqcount = 0;
		for (DTEquip de : eqlst){
			Equip eq = new Equip();
			eq.setUserId(acc.getId());
			eq.setHeroId(0);
			eq.setDictId(de.getEquipId());
			saveeqlst.add(eq);
			eqcount++;
			if (eqcount > 5){
				break;
			}
		}
		
		HibernateUtil.saveObjectsAndCommit(saveeqlst);
		
		PBCommand.S2CLogin.Builder resp = PBCommand.S2CLogin.newBuilder();
		resp.setToken(acc.getToken());
		
		PBMessage.PBUser.Builder pbu = PBMessage.PBUser.newBuilder();
		pbu.setUserId(acc.getId());
		pbu.setUserName(acc.getUserName());
		pbu.setLevel(acc.getLevel());
		pbu.setExp(acc.getExp());
		pbu.setGold(acc.getGold());
		pbu.setGem(acc.getGem());

		resp.setUserInfo(pbu.build());

		send(resp.build());
	}
}
