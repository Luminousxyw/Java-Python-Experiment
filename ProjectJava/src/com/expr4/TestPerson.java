package com.expr4;

import java.util.*;

public class TestPerson {
    public static void main(String[] args) {
        ArrayList<StudentEx> students = new ArrayList<>();
        students.add(new StudentEx("Alice", 20, 85.5, "Class1"));
        students.add(new StudentEx("Bob", 21, 92.0, "Class1"));
        students.add(new StudentEx("Charlie", 19, 55.0, "Class2"));
        students.add(new StudentEx("David", 20, 76.5, "Class2"));
        students.add(new StudentEx("Eve", 22, 95.5, "Class1"));

        students.sort((a, b) -> Double.compare(b.getScore(), a.getScore()));
        System.out.println("Sorted by score desc:");
        for (StudentEx s : students) {
            s.showInfo();
        }

        System.out.println("\nStudents with score >= 60:");
        ArrayList<StudentEx> passed = new ArrayList<>();
        for (StudentEx s : students) {
            if (s.getScore() >= 60) {
                passed.add(s);
                s.showInfo();
            }
        }

        System.out.println("\n--- Extended experiment ---");
        System.out.println("Award check:");
        for (StudentEx s : students) {
            System.out.println(s.getAward());
        }

        HashMap<String, List<StudentEx>> classMap = new HashMap<>();
        for (StudentEx s : students) {
            classMap.computeIfAbsent(s.getClassName(), k -> new ArrayList<>()).add(s);
        }

        System.out.println("\nGrouped by class:");
        for (Map.Entry<String, List<StudentEx>> entry : classMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}