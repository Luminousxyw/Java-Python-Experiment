package com.expr3;

public class UnionPay implements Payable, Refundable {
    private String cardNo;

    public UnionPay(String cardNo) {
        this.cardNo = cardNo;
    }

    @Override
    public boolean pay(double amount) {
        if (amount > 0) {
            System.out.println("银联卡号" + cardNo + "支付" + amount + "元成功");
            return true;
        } else {
            System.out.println("支付金额非法");
            return false;
        }
    }

    @Override
    public void showPayInfo() {
        System.out.println("支付方式：银联支付，卡号：" + cardNo);
    }

    @Override
    public boolean refund(double amount) {
        if (amount > 0) {
            System.out.println("银联卡号" + cardNo + "退款" + amount + "元成功");
            return true;
        } else {
            System.out.println("退款金额非法");
            return false;
        }
    }

    @Override
    public void showRefundInfo() {
        System.out.println("退款方式：银联支付，卡号：" + cardNo);
    }

    public String getCardNo() {
        return cardNo;
    }

    public void setCardNo(String cardNo) {
        this.cardNo = cardNo;
    }
}