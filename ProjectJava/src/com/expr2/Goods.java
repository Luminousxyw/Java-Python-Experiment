package com.expr2;
public class Goods {
    private String name;
    private double price;
    private int stock;
    public Goods(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        setStock(stock);
    }
    public String getGoodsInfo() {
        return "商品名：" + name + "，单价：" + price + "元，库存：" + stock + "件";
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getPrice() {
        return price;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public int getStock() {
        return stock;
    }
    public void setStock(int stock) {
        if (stock >= 0) {
            this.stock = stock;
        } else {
            this.stock = 0;
            System.out.println("库存不能为负数");
        }
    }
    @Override
    public String toString() {
        return getGoodsInfo();
    }
}