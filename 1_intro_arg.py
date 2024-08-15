# with the help of * arg we can make a flexible func

# for ex:

def check(a,b):
    return a+b
print(check(4,4))
# print(total(4,4,3))
# look here we cant add or more multiply more than two variable 
# if we wanna do we have to give more parameter as per the arguments
# to make it easy we use *arg as a parameter ,with the help of this we can do whatever we want to do in func
# this word done by *(star) we can use any word instead of args
# this star method gives tuple.
def new(*args):
    print(args)
    print(type(args))
new(1,3,5,7,9,10)

# we gonna do sum 
# first we have to def a func and then create a variable with 0 value
#after that do a for loop and add the value in the created value and then return it and  do print
# we can add or substract by changing the sign in the created variable
def all_total(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(all_total(2,2))