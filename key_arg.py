def add(a, b, c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    sum = a+b+c+d
    return(sum)

# ans = add(10,20,30,40)
ans = add(a=1,b=20,c=3,d=4)
print(ans)

def info(name, age=50):
    print("name: ", name)
    print("age: ", age)
    return()

info(age=25, name="Varsha")
info(name='worrier')

def employee(name, id, salary=10000):
    print("name:",name)
    print("id:", id)
    print("salary:", salary)
    return()

employee(name="Jonny", id=1)
employee(name="worrier", id =2, salary=520000)

# ------- variable - lenght arrguments

def info(user, *users):
    print("user of python:",user)
    # print(user)
    for var in users:
        print("User of Python", var)
        # print(var)
        # return()

# info("Annie")
info("Annie","Dave","asd","ewer")

def comp(id, *desig):
    print("Differnet desiignation", id)

    for d in desig:
        print("This is the designation:", d)

comp('Hr','It','manager','client','service')

# ----------- passing key-word arguments

def muFunction(arg1, arg2, arg3, *args, **kwargs):
    print("First normal argumrets:" + str(arg1))
    print("second normal argumnets:" + str(arg2))
    print("Third normal arguments:" + str(arg3))
    print("non-keywords arguments:"+ str(args))
    print("keywords arguments:"+ str(kwargs))
 
muFunction(1,2,3,4,5,6,name='varsha', country='India', age=25)
