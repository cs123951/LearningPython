class Super:
    def method(self):
        print("in Super.method  ")

    def delegate(self):
        self.action()  # 在子类中期待一个动作

    def action(self):
        # 抽象超类：类的部分行为默认是由子类所提供的
        raise NotImplementedError('action must be defined!')


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print("in Replacer.method  ")


class Extender(Super):
    def method(self):
        print("start Extender.method  ")
        Super.method(self)
        print("end Extender.method  ")


class Provider(Super):
    def action(self):
        print("in Provider.action  ")


if __name__ == "__main__":
    for kclass in (Super, Inheritor, Replacer, Extender, Provider):
        print("\n"+kclass.__name__+"...")
        kclass().method()
    print("\nProvider...")
    x = Provider()
    # 在Provider中找delegate，然后到Super中搜索，Super中需要调用self.action()
    # 此时在Super中，self指的是Provider实例，因此还是先从Provider开始，由下到上搜索
    x.delegate()
