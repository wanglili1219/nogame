package com.ease.nogame.handler;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import com.ease.nogame.domain.Hero;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class HeroInfoHandler extends MessageHandler {

	@Override
	public void handle(Message msg) {
		Session s = HibernateUtil.currentSession();
		Query q = s.getNamedQuery("queryHeroByUserId");
		q.setLong("userId", getUserId());
		List<Hero> hlst = q.list();
		List<PBMessage.PBHero> rlst = new ArrayList<PBMessage.PBHero>();
		for (Hero h : hlst){
			PBMessage.PBHero.Builder hb = PBMessage.PBHero.newBuilder();
			hb.setHeroId(h.getId());
			hb.setDictId(h.getDictId());
			hb.setLevel(h.getLevel());
			hb.setExp(h.getExp());
			rlst.add(hb.build());
		}

		PBCommand.S2CHeroInfo.Builder resp = PBCommand.S2CHeroInfo.newBuilder();
		resp.addAllHeroList(rlst);
		
		send(resp.build());
	}

}
