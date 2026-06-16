package com.expr2;

public class Rectangle {
    private double length;
    private double width;
    public Rectangle(){
        this.length=1.0;
        this.width=1.0;
    }
    public Rectangle(double length,double width){
        if(length>=0&&width>=0){
            this.length=length;
            this.width=width;
        }
        else{
            this.length=1.0;
            this.width=1.0;
        }
    }
    public double getArea(){
        return length*width;
    }
    public double getPerimeter(){
        return 2*(length+width);
    }
    public void setSize(double len) {
        if (len < 0) {
            System.out.println("边长不能为负数");
        } else {
            this.length = len;
            this.width = len;
        }
    }
    public void setSize(double len, double wid) {
        if (len < 0) {
            System.out.println("长不能为负数");
        } else {
            this.length = len;
        }
        if (wid < 0) {
            System.out.println("宽不能为负数");
        } else {
            this.width = wid;
        }
    }
    public double getLength() {
        return length;
    }
    public void setLength(double length) {
        if (length < 0) {
            System.out.println("边长不能为负数");
        } else {
            this.length = length;
        }
    }
    public double getWidth() {
        return width;
    }
    public void setWidth(double width) {
        if (width < 0) {
            System.out.println("边长不能为负数");
        } else {
            this.width = width;
        }
    }
    public boolean isSquare(){
        if(this.length==this.width){
            return true;
        }
        else{
            return false;
        }
    }
}
