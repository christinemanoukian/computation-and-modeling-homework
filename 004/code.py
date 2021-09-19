def func(x, n, num):
    return x ** n - num

def deriv(x, n):
    return n * x ** (n-1) 

def newton_rhapson(x, n, precision):
    x_old = 1
    condition = True
    while condition:
        if deriv(x_old, n) == 0:
            print("can't divide by zero")
            break
        else:
            x_new = x_old - func(x_old, n, x) / deriv(x_old, n)
            x_old = x_new
        condition = abs(func(x_new, n, x)) >= precision
    return x_old
