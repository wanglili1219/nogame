package com.ease.nogame.util;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
	public static SessionFactory sessionFactory = null;
	public static ThreadLocal threadSlot = new ThreadLocal();

	static {
		try {
			Configuration configuration = new Configuration().configure();
			sessionFactory = configuration.buildSessionFactory();
		} catch (Throwable ex) {
			ex.printStackTrace();
			System.err.println("Initial SessionFactory creation failed." + ex);
		}
	}

	public static Session currentSession() throws HibernateException {
		Session s = (Session) threadSlot.get();
		if (s == null) {
			s = sessionFactory.openSession();
			threadSlot.set(s);
		}
		
		return s;
	}

	public static void closeSession() throws HibernateException {
		Session s = (Session) threadSlot.get();
		if (s != null){
			s.close();
		}
		
		threadSlot.set(null);
		threadSlot = null;
	}
	

	public static void saveAndCommit(Object obj){
		Session s = currentSession();
		s.beginTransaction();
		s.save(obj);
		s.getTransaction().commit();
	}

}
