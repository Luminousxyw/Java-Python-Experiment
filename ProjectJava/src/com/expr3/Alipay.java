package com.expr3;

public class Alipay implements Payable {
    private String account;

    public Alipay(String account) {
        this.account = account;
    }

    @Override
    public boolean pay(double amount) {
        if (amount > 0) {
            System.out.println("支付宝账号" + account + "支付" + amount + "元成功");
            return true;
        } else {
            System.out.println("支付金额非法");
            return false;
        }
    }

    @Override
    public void showPayInfo() {
        System.out.println("支付方式：支付宝，账号：" + account);
    }

    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }
}