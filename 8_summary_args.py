def add(a,b):
    return a+b
print(add(2,3))
# here we can see that we cant add or subs more than two arguments
# to add more arguments we use *args method

def new_add(*args):
   total = 0
   for i in args:
       total +=i
   return total
print(new_add(1,2,4,6,7))

# we can use other words insteadd 0f the args the main func done by *
# in this method first we have to assign a varibale
# and start for loop and add the value and return it and print.
def new_add(*args):
   total = 0
   for i in args:
       total +=i
   return total
l=[1,2,4,6,7]
print(new_add(*l))
# if u wanna add parameter in argument we have to use * method
# we can use list or tuples
# this is the way to unpacking the list or tuples

# kwargs - keyword arguments, ** 
# this method return dict 
def new(**kwargs):
    print(kwargs)
    print(type(kwargs))
new(name='mehraj',age=23)

# now if u wanna use all parameters like
# normal parameter 
# *args
# default parameter
# ** kwargs
# this is the order that we have to use otherwise error will occur
def func2(name,*args,age = 23,**kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
func2('mehraj',1,13,3,a=2,s=6) 
