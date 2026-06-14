package com.expr3;

public class Bird extends Animal implements Runnable {
    private boolean canFly;

    public Bird(String name, int age, boolean canFly) {
        super(name, age);
        this.canFly = canFly;
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + "叽叽喳喳叫");
    }

    @Override
    public void run() {
        System.out.println(getName() + "慢悠悠奔跑");
    }

    public void fly() {
        if (canFly) {
            System.out.println(getName() + "在空中飞翔");
        } else {
            System.out.println(getName() + "不会飞");
        }
    }

    public boolean isCanFly() {
        return canFly;
    }

    public void setCanFly(boolean canFly) {
        this.canFly = canFly;
    }
}