class SharedData:
    spam = 42  # 数据属性，在顶层，为所有实例共享


class MixedNames:
    data = 'spam'  # 类对象的属性，在实例继承变量名的类中

    def __init__(self, value):
        # self返回的是调用主题，也就是实例对象，一个类有多个实例对象
        self.data = value  # 在实例对象中

    def display(self):
        print(self.data, MixedNames.data)  # 这两个display是不一样的


if __name__ == "__main__":
    x = SharedData()
    y = SharedData()
    print(x.spam, y.spam)
    SharedData.spam = 98  # 对类进行修改，影响所有实例的值
    print(x.spam, y.spam)
    x.spam = 54  # 对实例进行修改，不影响其他实例的值
    print(x.spam, y.spam)

    z = MixedNames(1)
    zz = MixedNames(2)
    z.display()  # 自动把实例方法对应到类函数
    zz.display()  # 调用方法1：通过实例调用
    MixedNames.display(zz)  # 调用方法2：通过类调用
