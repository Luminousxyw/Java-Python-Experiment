package com.expr2;

public class TestRectangle {
    public static void main(){
        Rectangle rect1=new Rectangle();
        System.out.println("rect1的面积和周长为："+rect1.getArea()+" and "+rect1.getPerimeter());
        Rectangle rect2=new Rectangle(5.0,-3.0);
        System.out.println("rect2的面积和周长为："+rect2.getArea()+" and "+rect2.getPerimeter());
        rect1.setSize(4.0);
        System.out.println("修改后rect1的面积和周长为："+rect1.getArea()+" and "+rect1.getPerimeter());
        rect2.setSize(-2.0,4.0);
        System.out.println("修改后rect2的面积和周长为："+rect2.getArea()+" and "+rect2.getPerimeter());
        System.out.println("rect1"+(rect1.isSquare()?"是":"不是")+"正方形");
        Rectangle rect3=new Rectangle(8.0,8.0);
        System.out.println("rect3"+(rect3.isSquare()?"是":"不是")+"正方形");
    }
}
