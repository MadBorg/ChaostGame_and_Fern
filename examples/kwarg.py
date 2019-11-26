class test:
    def __init__(self, **kwargs):
        self.args = kwargs

    def __call__(self, fun):
        fun(**self.args)



def fun1(a, b):
    print (a, b)

f = test()
# f(fun1)
