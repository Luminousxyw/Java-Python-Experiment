package com.expr3;

public class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        if (radius > 0) {
            this.radius = radius;
        } else {
            this.radius = 1.0;
        }
    }

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        if (radius > 0) {
            this.radius = radius;
        } else {
            this.radius = 1.0;
        }
    }
}