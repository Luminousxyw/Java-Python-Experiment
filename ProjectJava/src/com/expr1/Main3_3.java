package com.expr1;
import java.util.stream.IntStream;
public class Main3_3 {
    public static void main(String[] args) {
        int sum = IntStream.rangeClosed(1, 999)   // 生成 1~999 的整数流
                .filter(n -> n % 2 == 1)          // 过滤出奇数
                .sum();                           // 求和

        System.out.println("1+3+5+...+999 = " + sum);  // 输出 250000
    }
}
