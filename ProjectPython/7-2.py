from datetime import datetime


class User:
    """顶层父类: 普通用户"""

    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.register_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def login(self):
        print(f"用户{self.username}登录成功")

    def view_product(self, product_name, price):
        print(f"{self.username}查看商品: {product_name} 价格: {price}")

    def show_info(self):
        print(f"用户名:{self.username} ID:{self.user_id} 注册时间:{self.register_time}")


class VipUser(User):
    """会员用户"""

    def __init__(self, username, user_id, vip_level, points=0):
        super().__init__(username, user_id)
        self.vip_level = vip_level
        self.points = points

    def view_product(self, product_name, price):
        discounted = price * 0.9
        print(f"{self.username}(VIP{self.vip_level})查看商品: {product_name} "
              f"原价:{price} 会员价:{discounted:.2f}")

    def add_points(self, amount):
        self.points += amount
        print(f"{self.username}获得{amount}积分,当前积分:{self.points}")


class ShopOwner:
    """商家类"""

    def __init__(self, shop_name):
        self.shop_name = shop_name

    def manage_shop(self):
        print(f"商家{self.shop_name}管理店铺")

    def view_product(self, product_name, price):
        print(f"商家查看自家商品: {product_name} 成本价: {price * 0.6}")


class AdminUser(VipUser, ShopOwner):
    """管理员用户,多继承"""

    def __init__(self, username, user_id, vip_level, admin_level, shop_name, points=0):
        VipUser.__init__(self, username, user_id, vip_level, points)
        ShopOwner.__init__(self, shop_name)
        self.admin_level = admin_level

    def show_info(self):
        super().show_info()
        print(f"管理员等级:{self.admin_level} 管理店铺:{self.shop_name}")
        print(f"VIP等级:{self.vip_level} 积分:{self.points}")

    def delete_user(self, target_user):
        if self.admin_level >= 3:
            print(f"管理员{self.username}删除用户{target_user}")
        else:
            print(f"权限不足,需要3级以上管理员")

    def change_price(self, product_name, new_price):
        print(f"管理员{self.username}将{product_name}价格修改为{new_price}")


def create_user_by_type():
    """根据输入自动创建对应类型的对象"""
    user_type = input("选择用户类型(1普通 2会员 3管理员): ")
    name = input("用户名: ")
    uid = input("用户ID: ")
    if user_type == "2":
        level = input("会员等级: ")
        return VipUser(name, uid, level)
    elif user_type == "3":
        v_level = input("会员等级: ")
        a_level = int(input("管理员等级: "))
        shop = input("店铺名: ")
        return AdminUser(name, uid, v_level, a_level, shop)
    else:
        return User(name, uid)


def test():
    print("基础部分")
    u1 = User("小明", "U001")
    u1.login()
    u1.view_product("手机", 3000)
    u1.show_info()

    print()
    v1 = VipUser("小红", "V001", "金卡")
    v1.login()
    v1.view_product("手机", 3000)
    v1.add_points(100)
    v1.show_info()

    print()
    admin = AdminUser("管理员", "A001", "钻石", 5, "旗舰店")
    admin.login()
    admin.view_product("手机", 3000)
    admin.show_info()
    admin.delete_user("U001")
    admin.change_price("手机", 2800)

    print("\n扩展部分")
    print("MRO(方法解析顺序):", [c.__name__ for c in AdminUser.__mro__])

    admin2 = AdminUser("低级管理员", "A002", "金卡", 1, "小店")
    admin2.delete_user("U001")

    print("\n动态创建用户:")
    new_user = create_user_by_type()
    new_user.show_info()


if __name__ == "__main__":
    test()