from classtools import AttrDisplay


# AttrDisplay 成为一个通用工具，可以被任何类继承
class Person(AttrDisplay):
    # 实例构造函数，self是新创建的实例对象，当产生实例的时候，会自动调用__init__()函数，初始化实例
    def __init__(self, name, job=None, pay=1000):
        self.name = name  # self.name是实例的属性， name参数是__init__作用域的本地变量
        self.job = job
        self.pay = pay

    # 这是方法
    def splitName(self):
        return self.name.split("u")

    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))

    # 运算符重载：一个实例可以通过定义具有特殊名称的方法，来实现由特殊语法引发的特定操作
    # def __str__(self):
    #     return 'PERSON: %s %s %s' %(self.name, self.job, self.pay)


# 编写子类, 继承了Person
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "manager", pay)

    # 直接调用最初的版本，这样只需要改一个文件了
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)


# 可能聚合其他对象，并把它们当做一个集合
class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == "__main__":
    susan = Person("susan", "teacher", 1000)
    steve = Manager("steve", 100000)
    steve.giveRaise(0.2)
    development = Department()
    development.addMember(susan)
    development.addMember(steve)
    development.showAll()
    print(steve.__class__) # 提供了一个从实例到创建它的类的链接
    print(steve.__class__.__name__) # 提供了类的名称
    print(steve.__class__.__bases__)  # 提供了超类的访问
    print(list(steve.__dict__.keys())) # 类的属性
