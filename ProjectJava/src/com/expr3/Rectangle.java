package com.expr3;

public class Rectangle extends Shape {
    private double length;
    private double width;

    public Rectangle(double length, double width) {
        if (length > 0) {
            this.length = length;
        } else {
            this.length = 1.0;
        }
        if (width > 0) {
            this.width = width;
        } else {
            this.width = 1.0;
        }
    }

    @Override
    public double calculateArea() {
        return length * width;
    }

    @Override
    public double calculatePerimeter() {
        return 2 * (length + width);
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        if (length > 0) {
            this.length = length;
        }
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        if (width > 0) {
            this.width = width;
        }
    }
}