## ----single inheritance

class base1:
    def fun(self):
        print("This is the base class")

class sub(base1):
    pass

ob = sub()
ob.fun()



class dad:
    def quality(self):
        print("This is dad quality")

class child(dad):
    def up(self):
        print("child quality")
    

obj =child()
obj.quality()
obj.up()


##------------------------------ Multiple Inheritance

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("First")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
    print("Third")

Third();
