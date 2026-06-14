package com.expr3;

public class TestShape {
    public static void main(String[] args) {
        Circle circle = new Circle(5.0);
        circle.showShapeInfo();

        Rectangle rectangle = new Rectangle(4.0, 3.0);
        rectangle.showShapeInfo();

        Triangle triangle1 = new Triangle(3.0, 4.0, 5.0);
        triangle1.showShapeInfo();

        Triangle triangle2 = new Triangle(1.0, 2.0, 4.0);
        triangle2.showShapeInfo();

        Shape[] shapes = {circle, rectangle, triangle1, triangle2};
        for (Shape s : shapes) {
            s.showShapeInfo();
        }
    }
}