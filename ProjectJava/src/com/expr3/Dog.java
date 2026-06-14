package com.expr3;

public class Dog extends Animal implements Swimmable, Runnable {
    public Dog(String name, int age) {
        super(name, age);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + "汪汪叫");
    }

    @Override
    public void swim() {
        System.out.println(getName() + "在水里游泳");
    }

    @Override
    public void run() {
        System.out.println(getName() + "快速奔跑");
    }
}