
# def a func and take input as a num,iterable(list ,tuples) containing numbers as args

# example
# nums = [1,2,3]
# to_power(3,*num)

# output
# list--->[1**3,8,27]
# if user didnt pass any args then give a user a message "you didnt pass args"
# else return list 

def user(nums,*args):
    if args:
        return [i**nums for i in args]

    else:
        return "you didnt pass any args"
re = [1,2,3]
print(user(2,*re))    

