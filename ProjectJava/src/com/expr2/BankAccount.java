package com.expr2;

public class BankAccount {
    private String accountNo;
    private double balance;
    private String owner;
    private String pwd;
    private String tradeRecord;

    public BankAccount() {
        this("000000", "未知", 0.0);
    }

    public BankAccount(String accountNo, String owner) {
        this(accountNo, owner, 0.0);
    }

    public BankAccount(String accountNo, String owner, double balance) {
        this.accountNo = accountNo;
        this.owner = owner;
        if (balance < 0) {
            this.balance = 0;
            System.out.println("初始余额不能为负数");
        } else {
            this.balance = balance;
        }
        this.pwd = "123456";
        this.tradeRecord = "";
    }

    public void deposit(double money) {
        if (money > 0) {
            balance += money;
            recordTrade("存款 +" + money + "元，余额剩余" + balance + "元");
            System.out.println("存款成功：" + money + "元");
        } else {
            System.out.println("存款金额必须大于0");
        }
    }

    public void withdraw(double money) {
        if (money > 0 && money <= balance) {
            balance -= money;
            recordTrade("取款 -" + money + "元，余额剩余" + balance + "元");
            System.out.println("取款成功：" + money + "元");
        } else {
            System.out.println("取款金额非法或余额不足");
        }
    }

    public void showAccount() {
        System.out.println("开户人：" + owner + "，账户号：" + accountNo + "，余额：" + balance + "元");
    }

    public boolean verifyPwd(String inputPwd) {
        if (pwd != null && pwd.equals(inputPwd)) {
            return true;
        }
        return false;
    }

    public void transfer(BankAccount targetAccount, double money, String inputPwd) {
        if (!verifyPwd(inputPwd)) {
            System.out.println("密码错误");
            return;
        }
        if (money <= 0) {
            System.out.println("转账金额非法");
            return;
        }
        if (money > balance) {
            System.out.println("余额不足");
            return;
        }
        balance -= money;
        targetAccount.balance += money;
        String record = "向" + targetAccount.owner + "（" + targetAccount.accountNo
                      + "）转账" + money + "元，余额剩余" + balance + "元";
        recordTrade(record);
        targetAccount.recordTrade("收到" + owner + "（" + accountNo + "）转账" + money
                                + "元，余额剩余" + targetAccount.balance + "元");
        System.out.println("转账成功：" + money + "元 → " + targetAccount.owner);
    }

    public void showTradeRecord() {
        if (tradeRecord == null || tradeRecord.isEmpty()) {
            System.out.println("交易记录：暂无记录");
        } else {
            System.out.println("交易记录：\n" + tradeRecord);
        }
    }

    public void modifyPwd(String oldPwd, String newPwd) {
        if (!verifyPwd(oldPwd)) {
            System.out.println("旧密码错误");
            return;
        }
        if (newPwd == null || newPwd.length() < 6) {
            System.out.println("新密码长度不足6位");
            return;
        }
        this.pwd = newPwd;
        System.out.println("密码修改成功");
    }

    private void recordTrade(String record) {
        if (tradeRecord == null || tradeRecord.isEmpty()) {
            tradeRecord = record;
        } else {
            tradeRecord += "\n" + record;
        }
    }

    public String getAccountNo() {
        return accountNo;
    }

    public void setAccountNo(String accountNo) {
        this.accountNo = accountNo;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance < 0) {
            this.balance = 0;
            System.out.println("初始余额不能为负数");
        } else {
            this.balance = balance;
        }
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }

    public String getTradeRecord() {
        return tradeRecord;
    }

    public void setTradeRecord(String tradeRecord) {
        this.tradeRecord = tradeRecord;
    }
}