# functions in python 

def my_fun(a, b):
    result=a+b
    return(result)     #return should  be must in function. without return it can't to be  give output.
n=my_fun(34,67)
print(n)

#function using assign value to key

def gow_t(a,b):
    result=a-b
    return(result)
i=gow_t(a=32,b=24)
print(i)

#create a lambda functions in python 

kalai_cse=lambda a, b: a*b
o=kalai_cse(4,6)
print(o)

#create a function 

def real_r(numbers):
    result=(numbers)
    return(result)
numbers=24/6
i=real_r(numbers)
print(i)

#create a function using assign one value

def gow_t(a=23,b=10):  #if you assign value to be fine, but isn't considered while with function call.
    result=a-b
    return(result)
i=gow_t(a=115,b=15)    #actually the function will get the value from the function call
print(i)
