<<<<<<< HEAD
# when we def the func we called it parameters
# when we call the func we call it argument
def multiply_nums(*args):
    multiply = 1 #here the value should not be 0 otherwise the result will be zero
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,5,8))

def nums(new ,*args):
    multi = 1 
    print(new)
    print(args)
    for i in args:
        multi *= i
    return multi
print(nums(2,3,4))
# for ex:if we add one more parameter in def line
# look we add parameter(new) in print line the first number(2) is the argument of the new parameter 
# it will not multiply by 3 or 4
# we add more parameters beside the *args ,hence arguments as well
# we can add parameter on the left side of the *args 
# if we add parameters after *args you will get error
def number(n1,n2 ,*args):
    multi_ply = 1 
    for i in args:
        multi_ply *= i
    return multi_ply
print(number(2,2,5,4))
=======
# when we def the func we called it parameters
# when we call the func we call it argument
def multiply_nums(*args):
    multiply = 1 #here the value should not be 0 otherwise the result will be zero
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,5,8))

def nums(new ,*args):
    multi = 1 
    print(new)
    print(args)
    for i in args:
        multi *= i
    return multi
print(nums(2,3,4))
# for ex:if we add one more parameter in def line
# look we add parameter(new) in print line the first number(2) is the argument of the new parameter 
# it will not multiply by 3 or 4
# we add more parameters beside the *args ,hence arguments as well
# we can add parameter on the left side of the *args 
# if we add parameters after *args you will get error
def number(n1,n2 ,*args):
    multi_ply = 1 
    for i in args:
        multi_ply *= i
    return multi_ply
print(number(2,2,5,4))
>>>>>>> c17afe244925fd8b65651f30e37dbc57245ec3cd
