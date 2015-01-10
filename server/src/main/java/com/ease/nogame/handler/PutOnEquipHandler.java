package com.ease.nogame.handler;

import org.hibernate.Session;

import com.ease.nogame.domain.Equip;
import com.ease.nogame.domain.Hero;
import com.ease.nogame.gameserver.NGException;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class PutOnEquipHandler extends MessageHandler {

	@Override
	public void handle(Message msg) throws NGException {
		PBCommand.C2SPutOnEquip putonmsg = (PBCommand.C2SPutOnEquip)msg;
		long heroid = putonmsg.getHeroId();
		long equipid = putonmsg.getEquipId();
		
		Session s = HibernateUtil.currentSession();
		Equip equip = (Equip)s.get(Equip.class, equipid);
		if (equip == null){
			throw new NGException(100, "No found equip for equipId" + String.valueOf(equipid));
		}

		Hero hero = (Hero)s.get(Hero.class, heroid);
		if (hero == null){
			throw new NGException(100, "No found hero for heroId " + String.valueOf(heroid));
		}
		
		if (equip.getHeroId() != 0){
			throw new NGException(100, "Equip be weared by hero" + String.valueOf(equip.getHeroId()));
		}

		if (equip.getHeroId() == heroid){
			throw new NGException(100, "Equip already be weared by hero" + String.valueOf(equip.getHeroId()));
		}
		
		equip.setHeroId(hero.getId());
		HibernateUtil.saveAndCommit(equip);
		
		PBMessage.PBHero pbhero = Dao2PB.genPBHero(hero);
		PBCommand.S2CPutOnEquip.Builder respb = PBCommand.S2CPutOnEquip.newBuilder();
		respb.setHero(pbhero);
		
		send(respb.build());
	}

}
