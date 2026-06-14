package com.expr3;

public class Fish extends Animal implements Swimmable {
    public Fish(String name, int age) {
        super(name, age);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + "吐泡泡");
    }

    @Override
    public void swim() {
        System.out.println(getName() + "在水里游来游去");
    }
}