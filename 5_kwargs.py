# kwargs as a parameter
# the main func done by ** not the kwargs(we can use any name instead kwargs) 
# this ** return dictionary as a result
# we can do loop in this method as well
# we can call argument as much as you want.
# we can unpack the dict with this ** method
# for example 
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(first_name = "mehraj" ,  last_name = "khan")

def funct(**kwargss):
    for k,v in kwargss.items():
        print(f"{k}:{v}")

funct(first_name = "mehraj" ,  last_name = "khan")

# dictionary unpacking
def info(**kwargs):
    for k,v in kwargs.items():
       print(f"{k}:{v}")
d = {'gender':'male','age':23}
info(**d)