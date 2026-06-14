package com.expr2;

public class TestShoppingCart {

    public static void main(String[] args) {

        // 1. 创建3个商品对象
        Goods apple  = new Goods("苹果", 8.0, 50);
        Goods milk   = new Goods("牛奶", 5.5, 30);
        Goods bread  = new Goods("面包", 3.0, 20);

        System.out.println("已创建商品：");
        System.out.println(apple.getGoodsInfo());
        System.out.println(milk.getGoodsInfo());
        System.out.println(bread.getGoodsInfo());
        System.out.println();

        // 2. 创建购物车对象，测试 addGoods()
        ShoppingCart cart = new ShoppingCart();

        System.out.println(">>> 尝试添加苹果60件（库存50，应提示库存不足）：");
        cart.addGoods(apple, 60);

        System.out.println(">>> 尝试添加牛奶10件（库存30，应成功）：");
        cart.addGoods(milk, 10);

        System.out.println();

        // 3. 创建商品数组和数量数组，调用 calcTotal(Goods[], int[])
        Goods[] goodsArr = { apple, milk, bread };
        int[]   numArr   = { 5, 8, 3 };

        double total = cart.calcTotal(goodsArr, numArr);
        System.out.println("calcTotal(goodsArr, numArr) 计算结果：总金额 = " + total + "元");
        // 验证：5×8.0 + 8×5.5 + 3×3.0 = 40 + 44 + 9 = 93.0
        System.out.println("（预期：5×8.0 + 8×5.5 + 3×3.0 = 93.0元）");
        System.out.println();

        // 先看当前购物车内容（基本测试中已添加了牛奶10件）
        System.out.println("当前购物车内容（基本测试后的残留）：");
        cart.showCart();
        System.out.println();

        // 清空后重新开始扩展测试
        cart.clearCart();
        System.out.println();

        // 0. 将苹果和牛奶加入购物车（苹果5件，牛奶8件）
        System.out.println(">>> 添加苹果5件：");
        cart.addGoods(apple, 5);
        System.out.println(">>> 添加牛奶8件：");
        cart.addGoods(milk, 8);
        System.out.println();

        // 1. 计算初始总金额（无参 calcTotal）
        System.out.println(">>> 计算初始总金额（购物车内部）：");
        double initialTotal = cart.calcTotal();
        System.out.println("初始总金额 = " + initialTotal + "元");
        System.out.println("（预期：5×8.0 + 8×5.5 = 40 + 44 = 84.0元）");
        System.out.println();

        // 2. 修改牛奶数量为15，再次计算总金额
        System.out.println(">>> 修改牛奶数量为15：");
        cart.modifyNum(milk, 15);
        System.out.println(">>> 修改后计算总金额：");
        double totalAfterModify = cart.calcTotal();
        System.out.println("修改后总金额 = " + totalAfterModify + "元");
        System.out.println("（预期：5×8.0 + 15×5.5 = 40 + 82.5 = 122.5元）");
        System.out.println();

        // 3. 移除苹果，再次计算总金额
        System.out.println(">>> 移除苹果：");
        cart.removeGoods(apple);
        System.out.println(">>> 移除后计算总金额：");
        double totalAfterRemove = cart.calcTotal();
        System.out.println("移除后总金额 = " + totalAfterRemove + "元");
        System.out.println("（预期：15×5.5 = 82.5元）");
        System.out.println();

        // 4. 清空购物车，尝试计算总金额
        System.out.println(">>> 清空购物车：");
        cart.clearCart();
        System.out.println(">>> 清空后尝试计算总金额：");
        cart.calcTotal();  // 预期提示"购物车为空，总金额为0"
        System.out.println();

        // 测试库存校验
        System.out.println(">>> 测试 setStock 负数校验：");
        Goods testGoods = new Goods("测试商品", 10.0, -5);
        System.out.println("创建后库存应为0：" + testGoods.getGoodsInfo());
        System.out.println();

        // 测试 modifyNum 非法值
        System.out.println(">>> 重新添加商品后测试 modifyNum 边界：");
        cart.addGoods(apple, 10);   // 苹果库存50
        cart.modifyNum(apple, 0);   // 数量为0，非法
        cart.modifyNum(apple, -3);  // 数量为负，非法
        cart.modifyNum(apple, 100); // 超过库存50，非法
        cart.modifyNum(apple, 20);  // 合法
        System.out.println();

        // 测试数组长度不一致
        System.out.println(">>> 测试 calcTotal 数组长度不一致：");
        Goods[] shortArr = { apple, milk };
        int[]   longNums = { 1, 2, 3 };
        cart.calcTotal(shortArr, longNums);
        System.out.println();

    }
}