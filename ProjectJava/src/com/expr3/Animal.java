package com.expr3;

public abstract class Animal {
    private String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        if (age >= 0) {
            this.age = age;
        } else {
            this.age = 0;
        }
    }

    public abstract void makeSound();

    public void showAnimalInfo() {
        System.out.println("名称：" + name + "，年龄：" + age + "岁");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }
}