package com.ease.nogame.handler;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import com.ease.nogame.domain.Hero;
import com.ease.nogame.protobuf.PBApp;
import com.ease.nogame.protobuf.PBApp.PBHero;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class HeroInfoHandler extends MessageHandler {

	@Override
	public void handle(Message msg) {
		Session s = HibernateUtil.currentSession();
		Query q = s.getNamedQuery("queryHeroByUserId");
		q.setLong("userId", getUserId());
		List<Hero> hlst = q.list();
		List<PBHero> rlst = new ArrayList<PBHero>();
		for (Hero h : hlst){
			PBApp.PBHero.Builder hb = PBApp.PBHero.newBuilder();
			hb.setHeroId(h.getId());
			hb.setDictId(h.getDictId());
			hb.setLevel(h.getLevel());
			hb.setExp(h.getExp());
			rlst.add(hb.build());
		}

		PBApp.S2CHeroInfo.Builder resp = PBApp.S2CHeroInfo.newBuilder();
		resp.addAllHeroList(rlst);
		
		send(resp.build());
	}

}
