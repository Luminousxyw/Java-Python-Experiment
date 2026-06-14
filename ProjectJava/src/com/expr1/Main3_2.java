package com.expr1;
public class Main3_2 {
    public static void main(String[] args){
        int[] nums=new int[999];
        for(int i=0;i<999;i++){
            nums[i]=i+1;
        }
        int sum=0;
        for(int num:nums){
            sum+=num;
        }
        System.out.println(sum);
    }
}
