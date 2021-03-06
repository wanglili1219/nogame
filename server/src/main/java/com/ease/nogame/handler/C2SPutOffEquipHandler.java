package com.ease.nogame.handler;

import static com.ease.nogame.protobuf.PBCommand.*;

import org.hibernate.Session;

import com.ease.nogame.domain.Equip;
import com.ease.nogame.domain.Hero;
import com.ease.nogame.gameserver.NGErrorCode;
import com.ease.nogame.gameserver.NGException;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class C2SPutOffEquipHandler extends MessageHandler {
	
	@Override
	public void handle(Message msg) throws NGException {
		C2SPutOffEquip req = (C2SPutOffEquip) msg;
		long heroid = req.getHeroId();
		long equipid = req.getEquipId();
		Session s = HibernateUtil.currentSession();
		Hero hero = (Hero)s.get(Hero.class, heroid);
		if (hero == null){
			throw new NGException(NGErrorCode.NOT_FOUND_HERO, heroid);
		}
		
		Equip equip = (Equip)s.get(Equip.class, equipid);
		if (equip == null){
			throw new NGException(NGErrorCode.NOT_FOUND_EQUIP, equipid);
		}
		
		if (equip.getHeroId() != heroid){
			throw new NGException(NGErrorCode.HERO_NOT_HAS_EQUIP, 100, equipid);
		}
		
		equip.setHeroId(0);
		HibernateUtil.saveAndCommit(equip);
		
		S2CPutOffEquip.Builder respb = S2CPutOffEquip.newBuilder();
		respb.setHeroId(heroid);
		respb.setEquipId(equipid);
		
		send(respb.build());
	}
}
