## --------------aatributes private, public, ptotected

class edu():
    def __init__(self):
        self.__pri=("I am private")
        self._pro=("I am protected")
        self.pub=("I am public")

    def __privatemethod(self):
        print("In private")

ob = edu()
# print(ob.pub)
# print(ob._pro)
# print(ob.__pri)

ob._edu__privatemethod()
print(ob._edu__)

## -------------constructor, desctuctor, multiple constructor

class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    @classmethod
    def dmy(cls, day, month, year):
        cls.year = year
        cls.month = month
        cls.day = day
        return cls(cls.year, cls.month, cls.day)

    @classmethod
    def mdy(cls, month, day, year):
        cls.year = year
        cls.month = month
        cls.day = day

        return cls(cls.year, cls.month, cls.day)

a = Date(2016,12,11)
print(a.year)

b = Date.dmy(9,12,2020)
print(b.year)

c = Date.mdy(10,2,2018)
print(c.year)