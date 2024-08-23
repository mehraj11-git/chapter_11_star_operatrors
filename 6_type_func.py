# func can be default 
# we can do add ,subs, square in func
# parameters
# *agrs
# default parameter
# **kwargs
# PADK to remember this orders
def func(name,*args,last_name = "unknown",**kwargs):  #(1)
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func("mehraj",1,2,3,a=1,b=2)

# now look we call merhaj for name parameter
# gave numbers for args
# we donot give anything bcz the last_name is default 
# and for kwargs we gave argumnets in the form of dict bcz this method gives dict as a result
# we have to maintain the orders otherwise cant get the result
# (1) this is the order frist come name,then *operators,then default parameter,then **operators