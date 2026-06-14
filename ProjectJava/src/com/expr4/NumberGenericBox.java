package com.expr4;

public class NumberGenericBox<T extends Number> {
    private T data;

    public void setData(T data) {
        this.data = data;
    }

    public T getData() {
        return data;
    }

    public void showDataType() {
        if (data != null) {
            System.out.println("Data type: " + data.getClass().getName() + ", value: " + data);
        } else {
            System.out.println("Data is null");
        }
    }

    public double toDoubleValue() {
        if (data == null) {
            return 0.0;
        }
        return data.doubleValue();
    }
}