package com.expr1;
import java.math.BigDecimal;
import java.util.Scanner;
public class Main1_3 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入三个整数：");
        System.out.print("请输入第1个整数: ");
        BigDecimal num1 = sc.nextBigDecimal();
        System.out.print("请输入第2个整数: ");
        BigDecimal num2 = sc.nextBigDecimal();
        System.out.print("请输入第3个整数: ");
        BigDecimal num3 = sc.nextBigDecimal();
        BigDecimal min;
        if (num1.compareTo(num2) <= 0) {
            min = num1;
        } else {
            min = num2;
        }
        if (min.compareTo(num3) > 0) {
            min = num3;
        }
        System.out.println("最小的数是: " + min);
        sc.close();
    }
}
