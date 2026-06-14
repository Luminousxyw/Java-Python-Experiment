package com.expr3;

public abstract class Shape {
    public abstract double calculateArea();
    public abstract double calculatePerimeter();

    public void showShapeInfo() {
        System.out.println("图形类型：" + getClass().getSimpleName()
                + "，面积：" + calculateArea()
                + "，周长：" + calculatePerimeter());
    }
}