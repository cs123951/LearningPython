
# 当我们想要改变实例的显示，只要改变这个函数就行
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' %(key, getattr(self, key)))
        return ','.join(attrs)

    def __str__(self):
        return '%s %s'%(self.__class__.__name__, self.gatherAttrs())


if __name__ == "__main__":
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 1


    class SubTest(TopTest):
        pass

    x, y = TopTest(), SubTest()
    z = TopTest()
    print(x)
    print(y)
    print(z)
