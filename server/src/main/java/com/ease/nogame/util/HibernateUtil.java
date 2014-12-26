package com.ease.nogame.util;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.hibernate.service.ServiceRegistry;
import org.hibernate.service.ServiceRegistryBuilder;

public class HibernateUtil {
	public static SessionFactory sessionFactory = null;
	public static ThreadLocal threadSlot = new ThreadLocal();

	static {
		try {
			//Configuration configuration = new Configuration().configure();
			//sessionFactory = configuration.buildSessionFactory();

			Configuration configuration = new Configuration(); 
			configuration.configure(); 
			ServiceRegistry serviceRegistry = new ServiceRegistryBuilder().applySettings(configuration.getProperties()).buildServiceRegistry(); 
			sessionFactory = configuration.buildSessionFactory(serviceRegistry); 
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
	}
	

	public static void saveAndCommit(Object obj){
		Session s = currentSession();
		s.beginTransaction();
		s.save(obj);
		s.getTransaction().commit();
	}
}
