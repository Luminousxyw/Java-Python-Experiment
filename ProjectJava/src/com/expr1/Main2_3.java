package com.expr1;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main2_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = 0;
        boolean validInput = false;

        // 循环直到获取有效的1-12整数输入
        while (!validInput) {
            System.out.print("请输入一个1-12之间的整数: ");

            try {
                n = scanner.nextInt();

                // 验证整数是否在1-12范围内
                if (n >= 1 && n <= 12) {
                    validInput = true;
                } else {
                    System.out.println("错误：输入超出范围，请输入1-12之间的整数！");
                }
            } catch (InputMismatchException e) {
                System.out.println("错误：请输入有效的整数！");
                scanner.next(); // 清除无效输入
            }
        }

        // 根据月份判断季节
        switch (n) {
            case 1, 2, 12 -> System.out.println("冬季");
            case 3, 4, 5 -> System.out.println("春季");
            case 6, 7, 8 -> System.out.println("夏季");
            case 9, 10, 11 -> System.out.println("秋季");
        }

        scanner.close();
    }
}