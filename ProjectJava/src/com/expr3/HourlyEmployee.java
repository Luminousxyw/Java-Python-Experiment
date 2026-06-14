package com.expr3;

public class HourlyEmployee extends Employee {
    private double hourlyWage;
    private int hours;

    public HourlyEmployee(String id, String name, double hourlyWage, int hours) {
        super(id, name, 0);
        this.hourlyWage = hourlyWage;
        this.hours = hours;
    }

    @Override
    public double calculateSalary() {
        if (hours <= 40) {
            return hourlyWage * hours;
        } else {
            return hourlyWage * 40 + hourlyWage * (hours - 40) * 1.5;
        }
    }

    @Override
    public void showInfo() {
        System.out.println("小时工-编号：" + getId()
                + "，姓名：" + getName()
                + "，时薪：" + hourlyWage + "元"
                + "，工时：" + hours + "小时"
                + "，总薪资：" + calculateSalary() + "元");
    }

    public double getHourlyWage() {
        return hourlyWage;
    }

    public void setHourlyWage(double hourlyWage) {
        this.hourlyWage = hourlyWage;
    }

    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }
}