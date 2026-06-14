package com.expr1;

import java.util.Scanner;

public class Main5_1 {
    // 递归求斐波那契（基本数据类型 long）
    public static long fib(int n) {
        if (n == 1 || n == 2) {
            return 1;
        }
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入正整数 n（建议不超过50，否则递归极慢）: ");
        int n = scanner.nextInt();

        System.out.println("fib(" + n + ") = " + fib(n));

        // 测试：使用 long 类型时最大的 n 是多少
        System.out.println("\n测试 long 类型的最大 n :");
        for (int i = 1; i <= 100; i++) {
            long result = fib(i);
            System.out.println("n=" + i + " -> " + result);

            // long 类型溢出时值会变成负数
            if (result < 0) {
                System.out.println("当 n=" + i + " 时 long 类型溢出，最大有效 n=" + (i - 1));
                break;
            }
        }

        scanner.close();
    }
}