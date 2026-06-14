package com.expr1;
import java.util.Scanner;
public class Main2_2 {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        switch (n){
            case 1,2,12->System.out.println("冬季");
            case 3,4,5-> System.out.println("春季");
            case 6,7,8-> System.out.println("夏季");
            case 9,10,11-> System.out.println("秋季");
            default -> {
                break;
            }
        }
        scanner.close();
    }
}
