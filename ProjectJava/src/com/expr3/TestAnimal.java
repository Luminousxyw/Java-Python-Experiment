package com.expr3;

public class TestAnimal {
    public static void checkAbility(Animal animal) {
        if (animal instanceof Swimmable) {
            System.out.println(animal.getName() + "会游泳");
        }
        if (animal instanceof Runnable) {
            System.out.println(animal.getName() + "会奔跑");
        }
    }

    public static void main(String[] args) {
        Dog dog = new Dog("旺财", 3);
        dog.showAnimalInfo();
        dog.makeSound();
        dog.swim();
        dog.run();

        Fish fish = new Fish("小金鱼", 1);
        fish.showAnimalInfo();
        fish.makeSound();
        fish.swim();

        Bird bird1 = new Bird("麻雀", 2, true);
        bird1.showAnimalInfo();
        bird1.makeSound();
        bird1.run();
        bird1.fly();

        Bird bird2 = new Bird("鸵鸟", 4, false);
        bird2.showAnimalInfo();
        bird2.makeSound();
        bird2.run();
        bird2.fly();

        Animal[] animals = {dog, fish, bird1, bird2};
        for (Animal a : animals) {
            a.makeSound();
        }

        for (Animal a : animals) {
            checkAbility(a);
        }
    }
}