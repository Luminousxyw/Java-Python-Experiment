package com.expr4;

import java.util.*;

public class TestHashMap {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("ZhangSan", 85);
        map.put("LiSi", 92);
        map.put("WangWu", 58);
        map.put("ZhaoLiu", 76);
        map.put("SunQi", 88);

        System.out.println("ZhangSan score: " + map.get("ZhangSan"));

        map.put("WangWu", 65);
        System.out.println("After modifying WangWu: " + map.get("WangWu"));

        map.remove("ZhaoLiu");
        System.out.println("After removing ZhaoLiu, contains key? " + map.containsKey("ZhaoLiu"));

        System.out.println("\nTraversal by keys:");
        for (String key : map.keySet()) {
            System.out.println(key + " -> " + map.get(key));
        }

        System.out.println("\nTraversal by values:");
        for (Integer value : map.values()) {
            System.out.print(value + " ");
        }
        System.out.println();

        System.out.println("\nTraversal by entrySet:");
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }

        int count = 0;
        System.out.print("\nStudents with score >= 80: ");
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() >= 80) {
                System.out.print(entry.getKey() + " ");
                count++;
            }
        }
        System.out.println("\nCount of score >= 80: " + count);

        System.out.println("\n--- Extended experiment ---");
        extendedExperiment(map);
    }

    private static void extendedExperiment(HashMap<String, Integer> map) {
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort((a, b) -> b.getValue().compareTo(a.getValue()));
        System.out.println("Sorted by score desc:");
        for (Map.Entry<String, Integer> entry : list) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }

        int fail = 0, pass = 0, good = 0, excellent = 0;
        for (Integer score : map.values()) {
            if (score < 60) fail++;
            else if (score < 70) pass++;
            else if (score < 90) good++;
            else excellent++;
        }
        System.out.println("Score distribution: fail=" + fail + ", pass=" + pass + ", good=" + good + ", excellent=" + excellent);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter name to query (type 'exit' to stop):");
        while (true) {
            String input = scanner.nextLine().trim();
            if (input.equalsIgnoreCase("exit")) break;
            Integer score = map.get(input);
            if (score != null) {
                System.out.println(input + " score: " + score);
            } else {
                System.out.println("Student not found: " + input);
            }
        }
        scanner.close();
    }
}