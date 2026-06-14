package com.expr3;

public class Triangle extends Shape {
    private double side1;
    private double side2;
    private double side3;

    public Triangle(double side1, double side2, double side3) {
        if (isValidTriangle(side1, side2, side3)) {
            this.side1 = side1;
            this.side2 = side2;
            this.side3 = side3;
        } else {
            this.side1 = 1.0;
            this.side2 = 1.0;
            this.side3 = 1.0;
        }
    }

    private boolean isValidTriangle(double a, double b, double c) {
        return a > 0 && b > 0 && c > 0
                && a + b > c
                && a + c > b
                && b + c > a;
    }

    @Override
    public double calculateArea() {
        double s = (side1 + side2 + side3) / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    @Override
    public double calculatePerimeter() {
        return side1 + side2 + side3;
    }

    public double getSide1() {
        return side1;
    }

    public double getSide2() {
        return side2;
    }

    public double getSide3() {
        return side3;
    }

    public void setSide1(double side1) {
        if (isValidTriangle(side1, this.side2, this.side3)) {
            this.side1 = side1;
        }
    }

    public void setSide2(double side2) {
        if (isValidTriangle(this.side1, side2, this.side3)) {
            this.side2 = side2;
        }
    }

    public void setSide3(double side3) {
        if (isValidTriangle(this.side1, this.side2, side3)) {
            this.side3 = side3;
        }
    }
}