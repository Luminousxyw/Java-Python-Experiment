package com.expr1;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main5_2 {
    // 记忆化存储已计算的值
    private static Map<Integer, BigInteger> memo = new HashMap<>();

    // 递归算法（带记忆化）
    public static BigInteger fib(int n) {
        if (n == 1 || n == 2) {
            return BigInteger.ONE;
        }
        // 如果已计算过，直接返回
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        // 递归计算并存入记忆
        BigInteger result = fib(n - 1).add(fib(n - 2));
        memo.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("请输入正整数 n（1 < n < 10000，输入0退出）: ");
            int n = scanner.nextInt();

            if (n == 0) break;
            if (n <= 1 || n >= 10000) {
                System.out.println("错误：n 必须在 2 ~ 9999 之间！");
                continue;
            }

            memo.clear();  // 清空记忆
            BigInteger result = fib(n);
            System.out.println("fib(" + n + ") = " + result);
            System.out.println("位数: " + result.toString().length() + " 位\n");
        }

        scanner.close();
    }
}