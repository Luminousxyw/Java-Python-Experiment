package com.expr1;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main4_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 输入总人数 n 和报数 k
        System.out.print("请输入总人数 n: ");
        int n = scanner.nextInt();
        System.out.print("请输入报数 k: ");
        int k = scanner.nextInt();

        // 用列表存储玩家编号（1 ~ n）
        List<Integer> players = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            players.add(i);
        }

        int index = 0;  // 当前开始报数的位置（从0开始计数）
        System.out.println("\n淘汰顺序：");

        // while 循环，直到只剩一人
        while (players.size() > 1) {
            // 计算第 k 个人的索引
            index = (index + k - 1) % players.size();

            // 淘汰该玩家
            int eliminated = players.remove(index);
            System.out.println("淘汰玩家编号: " + eliminated);
        }

        // 输出胜利者
        System.out.println("\n胜利者是: " + players.get(0));

        scanner.close();
    }
}