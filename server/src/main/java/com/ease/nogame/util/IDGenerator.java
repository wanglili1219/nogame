package com.ease.nogame.util;

import org.apache.commons.lang3.RandomUtils;

public class IDGenerator {
    public final static int START_ID = 201500000;
        
    public static String generate() {
        int highRandBit = getRandBit();
        int lowRandBit = getRandBit();

        return generateId(1, highRandBit, lowRandBit);
    }

    private static String generateId(long countNumFromRedis, int highRandBit, int lowRandBit) {
        long countNumAfterAddStartNum = countNumFromRedis + START_ID;
        long lowThreeBits = countNumAfterAddStartNum % 100 + lowRandBit * 100;
        long midBits = countNumAfterAddStartNum / 100;
        String resultLowBit = String.valueOf(lowThreeBits + midBits * 1000);
        return highRandBit + resultLowBit;
    }

    private static int getRandBit() {
        return RandomUtils.nextInt(1, 10);
    }
}
