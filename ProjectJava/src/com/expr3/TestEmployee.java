package com.expr3;

public class TestEmployee {
    public static void main(String[] args) {
        Employee emp1 = new Employee("E001", "张三", 5000);
        emp1.showInfo();

        SalariedEmployee emp2 = new SalariedEmployee("E002", "李四", 6000, 2000);
        emp2.showInfo();

        HourlyEmployee emp3 = new HourlyEmployee("E003", "王五", 30, 45);
        emp3.showInfo();

        Employee[] employees = {emp1, emp2, emp3};
        for (Employee e : employees) {
            e.showInfo();
        }
    }
}