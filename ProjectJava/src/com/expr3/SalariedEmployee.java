package com.expr3;

public class SalariedEmployee extends Employee {
    private double bonus;

    public SalariedEmployee(String id, String name, double baseSalary, double bonus) {
        super(id, name, baseSalary);
        this.bonus = bonus;
    }

    @Override
    public double calculateSalary() {
        return getBaseSalary() + bonus;
    }

    @Override
    public void showInfo() {
        System.out.println("正式员工-编号：" + getId()
                + "，姓名：" + getName()
                + "，基本工资：" + getBaseSalary() + "元"
                + "，奖金：" + bonus + "元"
                + "，总薪资：" + calculateSalary() + "元");
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
}