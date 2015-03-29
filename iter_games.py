class MyClass:
    def __init__(self,l):
        self.l=l
    def __iter__(self):
        it = MyIter(self)
        return it


class MyIter:
    def __init__(self,MyClass):
        self.mc = MyClass
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        if self.index == len(self.mc.l):
            raise StopIteration
        self.index += 1
        return self.mc.l[self.index-1]


l = [1,2,3,4]
ll = MyClass(l)
for i in ll:
    for j in ll:
        print i,j

s = 'string'
ss = MyClass(s)
for c in ss:
    print c


