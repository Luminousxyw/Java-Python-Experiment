package com.expr3;

public class TestPay {
    public static void processPay(Payable payable, double amount) {
        payable.pay(amount);
        payable.showPayInfo();
    }

    public static void main(String[] args) {
        Alipay alipay = new Alipay("123456@aliyun.com");
        alipay.pay(100.0);
        alipay.showPayInfo();

        WechatPay wechatPay = new WechatPay("小码农");
        wechatPay.pay(-50.0);
        wechatPay.showPayInfo();

        UnionPay unionPay = new UnionPay("6228481234567890");
        unionPay.pay(200.0);
        unionPay.refund(50.0);
        unionPay.showPayInfo();
        unionPay.showRefundInfo();

        Payable[] payables = {alipay, wechatPay, unionPay};
        for (Payable p : payables) {
            p.pay(80.0);
        }

        processPay(alipay, 300.0);
        processPay(wechatPay, 150.0);
        processPay(unionPay, 500.0);
    }
}