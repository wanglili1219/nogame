/**
 * $Id: DateUtils.java 828427 2014-11-17 09:07:40Z huxiaowei $
 * Copyright(C) 2014-2020 netease - easegame, All Rights Reserved.
 */
package com.ease.nogame.util;

import java.util.Calendar;
import java.util.Date;

/**
 * 
 * @author <a href="mailto:huxiaowei@corp.netease.com">Xiaowei Hu</a>
 * @version 1.0 Sep 19, 2014 8:21:40 PM
 */
public class DateUtils {

    public static Date getNearbyHour(Date date) {
        Calendar c = Calendar.getInstance();
        c.setTime(date);
        c.clear(Calendar.MINUTE);
        c.clear(Calendar.SECOND);
        c.clear(Calendar.MILLISECOND);
        c.add(Calendar.HOUR, 1);
        return c.getTime();
    }
    
    public static Date getNextTime(Date now, int interval) {
        Date d = DateUtils.getNearbyHour(now);
        Calendar c = Calendar.getInstance();
        c.setTime(d);
        
        while (c.get(Calendar.HOUR_OF_DAY) % interval != 0) {
            c.add(Calendar.HOUR_OF_DAY, 1);
        }
        return c.getTime();
    }

    public static int getCurMonthDayNum(){  
        Calendar a = Calendar.getInstance();  
        a.set(Calendar.DATE, 1);
        a.roll(Calendar.DATE, -1);
        return a.get(Calendar.DATE);  
    }

    public static Date getCurMonthFirstDay(){
        Calendar a = Calendar.getInstance();  
        a.set(Calendar.DATE, 1);
        a.set(Calendar.HOUR_OF_DAY, 0);
        a.set(Calendar.MINUTE, 0);
        a.set(Calendar.SECOND, 0);
        return a.getTime();
    }

    public static Date getCurMonthLastDay(){
        Calendar a = Calendar.getInstance();  
        a.set(Calendar.DATE, 1);
        a.roll(Calendar.DATE, -1);
        a.set(Calendar.HOUR_OF_DAY, 23);
        a.set(Calendar.MINUTE, 59);
        a.set(Calendar.SECOND, 59);
        return a.getTime();
    }
    
}
