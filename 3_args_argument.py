# till now we learn how to use *args as a parameter
# in this exercise we will learn how to use *args as a arguement
def nums(*args):
    multi = 1 
    for i in args:
        multi *= i
    return multi

l = [2,4,2]
print(nums(l))
print(nums(*l))

# if i have a list for ex: l = [2,4,2]
# here the args will not work it will directly print the list
# to overcome this problem we have to add * [print(nums(*l)) <-----like this] 
#  with this it will unpack whether it will be a list or tuple