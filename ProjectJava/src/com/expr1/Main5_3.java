package com.expr1;

import java.math.BigInteger;
import java.util.Scanner;

public class Main5_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("请输入正整数 n（1 < n < 10000，输出杨辉三角行数，输入0退出）: ");
            int n = scanner.nextInt();

            if (n == 0) break;
            if (n <= 1 || n >= 10000) {
                System.out.println("错误：n 必须在 2 ~ 9999 之间！");
                continue;
            }

            // 使用 BigInteger 数组存储当前行
            BigInteger[] row = new BigInteger[1];
            row[0] = BigInteger.ONE;

            System.out.println("\n杨辉三角前 " + n + " 行：");

            for (int i = 0; i < n; i++) {
                // 显示行号（从第1行开始）
                System.out.print("第 " + (i + 1) + " 行: ");
                for (BigInteger num : row) {
                    System.out.print(num + " ");
                }
                System.out.println();

                // 计算下一行
                BigInteger[] nextRow = new BigInteger[i + 2];
                nextRow[0] = BigInteger.ONE;
                nextRow[nextRow.length - 1] = BigInteger.ONE;

                for (int j = 1; j < nextRow.length - 1; j++) {
                    nextRow[j] = row[j - 1].add(row[j]);
                }

                row = nextRow;
            }
            System.out.println();
        }

        scanner.close();
    }
}