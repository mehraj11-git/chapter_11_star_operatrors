# def  a func 
# this func take a input as a list and this return a list 
# but this list makes a first letter of the string capital 
# and check does this list give reverse str or not

def new_list(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return[name[::-1].title()for name in l]
    else:
        return[name.title()for name in l]
names = ["mehraj","khan"]

print(new_list(names,reverse_str=True))
print(new_list(names))
 

#  here we def two parameters and then we use get to access the kwargs whether it has reverse string or not
# and we used title method to make the first letter of the string in caps
# then use else statement then give arguments
