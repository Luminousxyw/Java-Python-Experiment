package com.example;
import java.util.Scanner; 
public class test {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int number = sc.nextInt();
        System.out.println(number);
        }
    }
}
