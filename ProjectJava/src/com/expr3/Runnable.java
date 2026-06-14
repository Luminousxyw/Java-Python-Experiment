package com.expr3;

public interface Runnable {
    void run();

    default boolean canRun() {
        return true;
    }
}