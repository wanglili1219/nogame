package com.ease.nogame.handler;

import static com.ease.nogame.protobuf.PBCommand.*;

import org.hibernate.Session;

import com.ease.nogame.domain.Equip;
import com.ease.nogame.domain.Hero;
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
			throw new NGException(100, "not found hero " + heroid);
		}
		
		Equip equip = (Equip)s.get(Equip.class, equipid);
		if (equip == null){
			throw new NGException(100, "not found equip " + equipid);
		}
		
		if (equip.getHeroId() != heroid){
			throw new NGException(100, "hero " + heroid + "not equip " + equipid);
		}
		
		equip.setHeroId(0);
		HibernateUtil.saveAndCommit(equip);
		
		S2CPutOffEquip.Builder respb = S2CPutOffEquip.newBuilder();
		respb.setHeroId(heroid);
		respb.setEquipId(equipid);
		
		send(respb.build());
	}
}
