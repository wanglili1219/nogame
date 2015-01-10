package com.ease.nogame.handler;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Query;

import com.ease.nogame.domain.*;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.protobuf.PBMessage.PBHero;
import com.ease.nogame.protobuf.PBMessage.PBHero.Builder;
import com.ease.nogame.util.HibernateUtil;


public class Dao2PB {
	public static PBHero genPBHero(Hero daoHero) {
		PBMessage.PBHero.Builder pbhero = PBMessage.PBHero.newBuilder();
		pbhero.setHeroId(daoHero.getId());
		pbhero.setDictId(daoHero.getDictId());
		pbhero.setExp(daoHero.getExp());
		pbhero.setLevel(daoHero.getLevel());

		Query qeq = HibernateUtil.currentSession().getNamedQuery("queryEquipByHeroId");
		qeq.setLong("heroId", daoHero.getId());
		List<Equip> elst = qeq.list();
		List<PBMessage.PBEquip> pbequilst = new ArrayList<PBMessage.PBEquip>();
		for (Equip eq : elst) {
			PBMessage.PBEquip.Builder eb = PBMessage.PBEquip.newBuilder();
			eb.setEquipId(eq.getId());
			eb.setDictId(eq.getDictId());
			eb.setHeroId(eq.getHeroId());
			pbequilst.add(eb.build());
		}

		pbhero.addAllEquipList(pbequilst);
		return pbhero.build();
	}
}
