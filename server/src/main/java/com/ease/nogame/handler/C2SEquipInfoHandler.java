package com.ease.nogame.handler;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import com.ease.nogame.domain.Equip;
import com.ease.nogame.protobuf.PBCommand;
import com.ease.nogame.protobuf.PBMessage;
import com.ease.nogame.util.HibernateUtil;
import com.google.protobuf.Message;

public class C2SEquipInfoHandler extends MessageHandler {

	@Override
	public void handle(Message msg) {
		Session s = HibernateUtil.currentSession();
		Query q = s.getNamedQuery("queryEquipByUserId");
		q.setLong("userId", getUserId());
		List<Equip> elst = q.list();
		List<PBMessage.PBEquip> resplst = new ArrayList<PBMessage.PBEquip>(); 
		for (Equip eq : elst){
			System.out.println("found equip" + String.valueOf(eq.getId()));
			PBMessage.PBEquip.Builder eqb = PBMessage.PBEquip.newBuilder();
			eqb.setEquipId(eq.getId());
			eqb.setDictId(eq.getDictId());
			eqb.setHeroId(eq.getHeroId());
			resplst.add(eqb.build());
		}
		
		PBCommand.S2CEquipInfo.Builder respb = PBCommand.S2CEquipInfo.newBuilder();
		respb.addAllEquipList(resplst);
		send(respb.build());
	}

}
