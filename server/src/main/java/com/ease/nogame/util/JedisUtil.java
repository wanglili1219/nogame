package com.ease.nogame.util;

import org.hibernate.exception.spi.Configurable;

import com.ease.nogame.gameserver.Configure;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

public class JedisUtil {
	private static JedisPool pool = null;
	
	public static boolean init(){
		JedisPoolConfig conf = new JedisPoolConfig();
		    JedisPoolConfig config = new JedisPoolConfig();
            conf.setMaxIdle(5);
            conf.setMaxWaitMillis(1000 * 100);
            String ip = Configure.getValue("jedis_ip");
            int port = Integer.valueOf((String) Configure.get("jedis_port"));
            pool = new JedisPool(conf, ip, port);	// 
            return true;
	}
	
	public static void tini(){
		if (pool != null){
			pool.destroy();
			pool = null;
		}
	}
	
	public static Jedis getJ(){
		assert(pool != null);
		return pool.getResource();
	}
	
	public static void returnJ(Jedis j){
		assert(pool != null);
		pool.returnResource(j);
	}
}
