package com.ease.nogame.gameserver;


import java.net.InetSocketAddress;
import java.nio.ByteOrder;


import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.LengthFieldBasedFrameDecoder;
import io.netty.handler.codec.LengthFieldPrepender;
import io.netty.handler.codec.protobuf.ProtobufDecoder;
import io.netty.handler.codec.protobuf.ProtobufEncoder;

import com.ease.nogame.domain.Customer;
import com.ease.nogame.protobuf.PBApp;

public class App 
{
	public static  class GameServer {
		  private static final int port = 8084;
		  private static final int NETWORK_FRAME_SIZE = 1024 * 1024 * 10;
	
		  public void start() throws InterruptedException {
		    ServerBootstrap b = new ServerBootstrap();
		    EventLoopGroup group = new NioEventLoopGroup();
		    try {
		      b.group(group);
		      b.channel(NioServerSocketChannel.class);
		      b.localAddress(new InetSocketAddress(port));
		      b.option(ChannelOption.SO_REUSEADDR, true);
		     
		      b.option(ChannelOption.SO_BACKLOG, 50);
		      b.childHandler(new ChannelInitializer<SocketChannel>() {
		            protected void initChannel(SocketChannel ch) throws Exception {
		            	ch.pipeline().addLast(new LengthFieldBasedFrameDecoder(ByteOrder.BIG_ENDIAN, NETWORK_FRAME_SIZE, 0, 4, 0, 4, true));
		            	ch.pipeline().addLast(new ProtobufDecoder(PBApp.MsgDesc.getDefaultInstance()));
						ch.pipeline().addLast(new LengthFieldPrepender(4));
		            	ch.pipeline().addLast(new ProtobufEncoder());
						ch.pipeline().addLast(new BaseChannelHandler());
					}
		          });

		      ChannelFuture f = b.bind().sync();
		      System.out.println("started and listen on " + f.channel().localAddress());
		      f.channel().closeFuture().sync();
		    } catch (Exception e) {
		      e.printStackTrace();
		    } finally {
		      group.shutdownGracefully().sync();
		    }
		  }
	}
	
    public static void main( String[] args )
    {
    	try {
            SessionFactory sf = new Configuration().configure().buildSessionFactory();
            Session session = sf.openSession();
            Transaction tx = session.beginTransaction();
           
            Customer customer = new Customer();
            customer.setAccountID(123);
            customer.setAddress("beijing");
            session.save(customer);

            tx.commit();
            session.close();

        } catch (HibernateException e) {
            e.printStackTrace();
        }

    	return;
//        try {
//        	MessageDispatcher.init(); 
//            GameServer es = new GameServer();
//            es.start();
//   	    } catch (InterruptedException e) {
//            e.printStackTrace();
//   	    }
    }
}
