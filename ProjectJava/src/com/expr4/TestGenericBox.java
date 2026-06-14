package com.expr4;

public class TestGenericBox {
    public static void main(String[] args) {
        GenericBox<Integer> intBox = new GenericBox<>();
        intBox.setData(100);
        System.out.println("Integer value: " + intBox.getData());
        intBox.showDataType();

        GenericBox<String> strBox = new GenericBox<>();
        strBox.setData("Hello Generics");
        System.out.println("String value: " + strBox.getData());
        strBox.showDataType();

        GenericBox<Double> doubleBox = new GenericBox<>();
        doubleBox.setData(3.14);
        System.out.println("Double value: " + doubleBox.getData());
        doubleBox.showDataType();

        System.out.println("\n--- NumberGenericBox ---");
        NumberGenericBox<Integer> numBox = new NumberGenericBox<>();
        numBox.setData(42);
        System.out.println("toDoubleValue: " + numBox.toDoubleValue());

        NumberGenericBox<Double> numBox2 = new NumberGenericBox<>();
        numBox2.setData(3.14159);
        System.out.println("toDoubleValue: " + numBox2.toDoubleValue());
    }
}