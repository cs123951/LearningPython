x = 11  # 模块属性


def f():
    print("f: "+str(x))  # 模块属性


def g():
    x = 22
    print("g: "+str(x))  # 函数中的本地变量


def g1():
    global x  # 全局变量，改变模块中的值
    x = 77
    print("global: "+ str(x))


def h1():
    x = 88
    def nested():
        print(x)
    nested()


def h2():
    x = 99
    def nested():
        nonlocal x  # 将变量声明为外层变量（外部函数的局部变量，而不是全局变量），可以在其外部修改名称
        x = 110
    nested()
    print("h2:"+str(x))


class C:
    x = 33  # 类属性

    def m(self):
        x = 44  # 方法中的本地变量
        self.x = 55  # 实例属性，赋值之后属性才会存在


if __name__ == "__main__":
    print(x)
    f()
    g()
    print(x)
    obj = C()
    print(C.x, obj.x)  # 在没给实例属性定义时，实例属性直接继承类的属性。
    obj.m()
    print(C.x, obj.x)

    g1()
    f()  # g1()改变了全局变量

    h1()
    h2()
    f()

