package com.expr3;

public class WechatPay implements Payable {
    private String nickname;

    public WechatPay(String nickname) {
        this.nickname = nickname;
    }

    @Override
    public boolean pay(double amount) {
        if (amount > 0) {
            System.out.println("微信昵称" + nickname + "支付" + amount + "元成功");
            return true;
        } else {
            System.out.println("支付金额非法");
            return false;
        }
    }

    @Override
    public void showPayInfo() {
        System.out.println("支付方式：微信支付，昵称：" + nickname);
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
}