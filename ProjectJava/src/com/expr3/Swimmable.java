package com.expr3;

public interface Swimmable {
    void swim();

    default boolean canSwim() {
        return true;
    }
}