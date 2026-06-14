package com.expr4;

public class GenericBox<T> {
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
}