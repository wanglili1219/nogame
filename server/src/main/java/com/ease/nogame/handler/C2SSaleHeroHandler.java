package com.ease.nogame.handler;

import java.util.List;

import org.hibernate.Session;

import com.ease.nogame.dict.DTHero;
import com.ease.nogame.dict.DTItem;
import com.ease.nogame.dict.DTManager;
import com.ease.nogame.domain.Account;
import com.ease.nogame.domain.Hero;
import com.ease.nogame.gameserver.NGErrorCode;
import com.ease.nogame.gameserver.NGException;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.protobuf.PBCommand.S2CSaleHero;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class C2SSaleHeroHandler extends MessageHandler {

	@Override
	public void handle(Message msg) throws NGException {
		PBCommand.C2SSaleHero req = (PBCommand.C2SSaleHero)msg;
		long heroid = req.getHeroId();
		Session s = HibernateUtil.currentSession();
		Hero hero = (Hero)s.get(Hero.class, heroid);
		if (hero == null){
			throw new NGException(NGErrorCode.NOT_FOUND_HERO, heroid);
		}
		
		final int herodictid = hero.getDictId();
		DTHero dthero = DTManager.HERO.getByID(herodictid);
		if (dthero == null){
			throw new NGException(NGErrorCode.NOT_FOUND_DICT_ID, herodictid);
		}
		
		DTItem dtitem = DTManager.ITEM.getByID(herodictid);
		if (dtitem == null){
			throw new NGException(NGErrorCode.NOT_FOUND_DICT_ID, herodictid);
		}

		int salegold = dtitem.getItemSalePrice() * hero.getLevel();
		Account acc = (Account) s.get(Account.class, getUserId());
		acc.setGold(acc.getGold() + salegold);

		s.beginTransaction();
		s.delete(hero);
		s.save(acc);
		s.getTransaction().commit();
		
		S2CSaleHero.Builder resp = S2CSaleHero.newBuilder();
		resp.setHeroId(heroid);
		resp.setSaleGold(salegold);
		send(resp.build());
	}

}
