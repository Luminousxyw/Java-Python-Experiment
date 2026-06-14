package com.expr2;
import java.util.ArrayList;
public class ShoppingCart {
    private ArrayList<Goods> cartGoods;
    private ArrayList<Integer> cartNums;
    public ShoppingCart() {
        cartGoods = new ArrayList<>();
        cartNums   = new ArrayList<>();
    }
    public void addGoods(Goods goods, int num) {
        if (goods == null) {
            System.out.println("商品不存在，添加失败");
            return;
        }
        if (num <= 0) {
            System.out.println("数量必须为正数，添加失败");
            return;
        }
        if (goods.getStock() >= num) {
            // 检查购物车中是否已有该商品，有则累加数量
            int index = cartGoods.indexOf(goods);
            if (index >= 0) {
                int oldNum = cartNums.get(index);
                cartNums.set(index, oldNum + num);
            } else {
                cartGoods.add(goods);
                cartNums.add(num);
            }
            System.out.println("添加成功：" + goods.getGoodsInfo() + " ×数量" + num);
        } else {
            System.out.println("库存不足，添加失败");
        }
    }
    public double calcTotal(Goods[] goodsList, int[] numList) {
        if (goodsList == null || numList == null) {
            System.out.println("参数不能为null");
            return 0.0;
        }
        if (goodsList.length != numList.length) {
            System.out.println("商品数组与数量数组长度不一致，无法计算");
            return 0.0;
        }
        double total = 0.0;
        for (int i = 0; i < goodsList.length; i++) {
            if (goodsList[i] != null && numList[i] > 0) {
                total += goodsList[i].getPrice() * numList[i];
            }
        }
        return total;
    }
    public double calcTotal() {
        if (cartGoods.isEmpty()) {
            System.out.println("购物车为空，总金额为0");
            return 0.0;
        }
        double total = 0.0;
        for (int i = 0; i < cartGoods.size(); i++) {
            total += cartGoods.get(i).getPrice() * cartNums.get(i);
        }
        return total;
    }
    public void removeGoods(Goods goods) {
        if (goods == null) {
            System.out.println("商品不存在，移除失败");
            return;
        }
        int index = cartGoods.indexOf(goods);
        if (index >= 0) {
            String goodsInfo = cartGoods.get(index).getGoodsInfo();
            cartGoods.remove(index);
            cartNums.remove(index);
            System.out.println("已移除商品：" + goodsInfo);
        } else {
            System.out.println("购物车中没有该商品：" + goods.getGoodsInfo());
        }
    }
    public void modifyNum(Goods goods, int newNum) {
        if (goods == null) {
            System.out.println("商品不存在，修改失败");
            return;
        }
        int index = cartGoods.indexOf(goods);
        if (index < 0) {
            System.out.println("购物车中没有该商品，修改失败");
            return;
        }
        if (newNum <= 0) {
            System.out.println("数量非法或库存不足");
            return;
        }
        if (newNum > goods.getStock()) {
            System.out.println("数量非法或库存不足");
            return;
        }
        cartNums.set(index, newNum);
        System.out.println("数量修改成功：" + goods.getGoodsInfo() + "，新数量：" + newNum);
    }
    public void clearCart() {
        cartGoods.clear();
        cartNums.clear();
        System.out.println("购物车已清空");
    }
    public void showCart() {
        if (cartGoods.isEmpty()) {
            System.out.println("购物车当前为空");
            return;
        }
        System.out.println("购物车清单");
        for (int i = 0; i < cartGoods.size(); i++) {
            System.out.println(cartGoods.get(i).getGoodsInfo() + " ×" + cartNums.get(i));
        }
        System.out.println();
    }
}
