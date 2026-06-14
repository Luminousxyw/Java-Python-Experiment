package com.expr4;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;

public class TestArrayList {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("ZhangSan");
        names.add("LiSi");
        names.add("WangWu");
        names.add("ZhaoLiu");
        names.add("SunQi");

        System.out.println("After adding 5 names:");
        printList(names);

        names.remove("LiSi");
        System.out.println("After removing LiSi:");
        printList(names);

        names.set(1, "ChenBa");
        System.out.println("After modifying index 1 to ChenBa:");
        printList(names);

        System.out.println("\nTraversal by for loop:");
        for (int i = 0; i < names.size(); i++) {
            System.out.print(names.get(i) + " ");
        }
        System.out.println();

        System.out.println("\nTraversal by enhanced for:");
        for (String name : names) {
            System.out.print(name + " ");
        }
        System.out.println();

        System.out.println("\nTraversal by iterator:");
        Iterator<String> it = names.iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
        System.out.println();

        Collections.sort(names);
        System.out.println("\nAfter dictionary sort:");
        printList(names);

        System.out.println("\n--- Extended experiment ---");
        extendedExperiment();
    }

    private static void printList(ArrayList<String> list) {
        System.out.println(list);
    }

    private static void extendedExperiment() {
        ArrayList<String> list = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter names (type 'exit' to stop):");
        while (true) {
            String input = scanner.nextLine().trim();
            if (input.equalsIgnoreCase("exit")) {
                break;
            }
            if (list.contains(input)) {
                System.out.println("Name already exists, not added: " + input);
            } else {
                list.add(input);
                System.out.println("Added: " + input);
            }
        }

        System.out.println("\nFinal list:");
        printList(list);

        if (!list.isEmpty()) {
            String longest = list.get(0);
            for (String name : list) {
                if (name.length() > longest.length()) {
                    longest = name;
                }
            }
            System.out.println("Longest name: " + longest);
        }
        scanner.close();
    }
}