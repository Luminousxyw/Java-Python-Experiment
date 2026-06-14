package com.expr2;

public class TestBankAccount {

    public static void main(String[] args) {

        BankAccount acc1 = new BankAccount();
        BankAccount acc2 = new BankAccount("6228481234567890", "王五");
        BankAccount acc3 = new BankAccount("6228489876543210", "赵六", -1000);

        System.out.println("三个账户的初始信息：");
        acc1.showAccount();
        acc2.showAccount();
        acc3.showAccount();
        System.out.println();

        System.out.println("对acc2（王五）执行操作：");

        System.out.print("存款-200元：");
        acc2.deposit(-200);

        System.out.print("存款1000元：");
        acc2.deposit(1000);
        acc2.showAccount();

        System.out.print("取款1500元：");
        acc2.withdraw(1500);

        System.out.print("取款800元：");
        acc2.withdraw(800);
        acc2.showAccount();
        System.out.println();

        System.out.print("为acc2修改密码(123456->654321)：");
        acc2.modifyPwd("123456", "654321");

        BankAccount acc4 = new BankAccount("6228481111111111", "钱七", 2000);
        System.out.println();

        System.out.print("用错误密码给钱七转账500元：");
        acc2.transfer(acc4, 500, "111111");

        System.out.print("用正确密码给钱七转账300元：");
        acc2.transfer(acc4, 300, "654321");
        System.out.println();

        System.out.println("转账后两个账户信息：");
        acc2.showAccount();
        acc4.showAccount();
        System.out.println();

        System.out.println("acc2交易记录：");
        acc2.showTradeRecord();
        System.out.println();

        System.out.println("acc4交易记录：");
        acc4.showTradeRecord();
        System.out.println();

        System.out.print("修改密码为123：");
        acc2.modifyPwd("654321", "123");

        System.out.print("修改密码为888888：");
        acc2.modifyPwd("654321", "888888");
        System.out.println();

        System.out.print("acc2向acc4转账-100元：");
        acc2.transfer(acc4, -100, "888888");

        System.out.print("acc2向acc4转账10000元(余额不足)：");
        acc2.transfer(acc4, 10000, "888888");

        System.out.print("acc2取款99999元：");
        acc2.withdraw(99999);

        System.out.print("acc3最终信息：");
        acc3.showAccount();
    }
}