package com.expr1;
import java.util.Scanner;
public class Main4_1 {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        while(n<30||n>80){
            System.out.print("please enter again: ");
            n=scanner.nextInt();
        }
        int i,sum=0;
        for(i=0;i<=n;i++){
            sum+=i;
        }
        System.out.println(sum);
    }
}
