class Test(object):

    var1 = 0

    def some(self):

        self.var1 = 2

    print(var1)
sol =  Test()
sol.some()
print(sol.var1)