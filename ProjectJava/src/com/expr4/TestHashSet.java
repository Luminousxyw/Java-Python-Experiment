package com.expr4;

import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;

public class TestHashSet {
    public static <T> void printCollection(Collection<T> coll) {
        for (T item : coll) {
            System.out.print(item + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        while (set.size() < 10) {
            int num = (int) (Math.random() * 20) + 1;
            set.add(num);
        }

        System.out.print("HashSet elements: ");
        printCollection(set);
        System.out.println("Size (unique count): " + set.size());
        System.out.println("Max: " + Collections.max(set));
        System.out.println("Min: " + Collections.min(set));

        System.out.println("\n--- Extended experiment ---");
        testStudentSet();
    }

    private static void testStudentSet() {
        HashSet<Student> students = new HashSet<>();
        students.add(new Student(101, "Alice"));
        students.add(new Student(102, "Bob"));
        students.add(new Student(101, "Alice2"));
        students.add(new Student(103, "Charlie"));
        students.add(new Student(102, "Bob2"));

        System.out.println("Students after dedup by id:");
        for (Student s : students) {
            System.out.println(s);
        }
        System.out.println("Student count: " + students.size());
    }
}