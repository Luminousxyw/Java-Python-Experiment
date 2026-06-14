package com.expr1;
import java.util.Scanner;
public class Main5_1 {
    public static long fibonacci(int n){
        if(n==1){
            return 1L;
        }
        else if(n==2){
            return 1L;
        }
        else{
            return fibonacci(n-1)+fibonacci(n-2);
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        long num=fibonacci(n);
        System.out.println(num);
        sc.close();
    }
}
