package com.ease.nogame.handler;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import com.ease.nogame.domain.Equip;
import com.ease.nogame.domain.Hero;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class HeroInfoHandler extends MessageHandler {

	@Override
	public void handle(Message msg) {
		Session s = HibernateUtil.currentSession();
		Query qhero = s.getNamedQuery("queryHeroByUserId");
		qhero.setLong("userId", getUserId());
		List<Hero> hlst = qhero.list();
		List<PBMessage.PBHero> rlst = new ArrayList<PBMessage.PBHero>();
		for (Hero h : hlst){
			PBMessage.PBHero.Builder hb = PBMessage.PBHero.newBuilder();
			hb.setHeroId(h.getId());
			hb.setDictId(h.getDictId());
			hb.setLevel(h.getLevel());
			hb.setExp(h.getExp());
			
			Query qeq = s.getNamedQuery("queryEquipByHeroId");
			qeq.setLong("heroId", h.getId());
			List<Equip> elst = qeq.list();
			List<PBMessage.PBEquip> pbequilst = new ArrayList<PBMessage.PBEquip>();
			for (Equip eq : elst){
				PBMessage.PBEquip.Builder eb = PBMessage.PBEquip.newBuilder();
				eb.setEquipId(eq.getId());
				eb.setDictId(eq.getDictId());
				eb.setHeroId(eq.getHeroId());
				pbequilst.add(eb.build());
			}
			
			hb.addAllEquipList(pbequilst);
			rlst.add(hb.build());
		}

		PBCommand.S2CHeroInfo.Builder resp = PBCommand.S2CHeroInfo.newBuilder();
		resp.addAllHeroList(rlst);

		send(resp.build());
	}

}
