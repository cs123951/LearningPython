import manynames


x = 66
print(x)  # 66
print(manynames.x)  # 11

manynames.f()  # 11，打印的是manynames的x，而不是本文件的x，作用域总是由源代码的赋值语句位置来决定的。
manynames.g()  # 22

print(manynames.C.x)  # 33
obj = manynames.C()
print(obj.x)  # 33
obj.m()
print(obj.x)  # 55