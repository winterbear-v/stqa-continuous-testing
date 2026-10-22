def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def divide(a,b):
    if b==0:
        raise ValueError("XX Cannot Divide by Zero XX")
    return a/b

def square(a):
    return a * a

def maximum(a,b):
    if a>b:
        return a
    else:
        return b