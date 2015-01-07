package com.ease.nogame.util;

import java.io.Serializable;


public class Item implements Serializable{
	

	private static final long serialVersionUID = 1L;
	private int type;
    private int id;
    private int count;
    private double rate;
    
    /**
     * @param type  类型
     * @param id    ID
     * @param count 数量 
     * @param rate  概率
     */
    public Item(int type, int id, int count, double rate) {
        super();
        this.type = type;
        this.id = id;
        this.count = count;
        this.rate = rate;
    }

    /**
     * @param type  类型
     * @param id    ID
     * @param count 数量 
     */
    public Item(int type, int id, int count) {
        this(type, id, count, 0);
    }

    public void setType(int type) {
        this.type = type;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public void setRate(double rate) {
        this.rate = rate;
    }

    public int getType() {
        return type;
    }
    
    public int getId() {
        return id;
    }
    
    public int getCount() {
        return count;
    }
    
    public double getRate() {
        return rate;
    }

    @Override
    public String toString() {
        return "Item [type=" + type + ", id=" + id + ", count=" + count + ", rate=" + rate + "]";
    }
}
