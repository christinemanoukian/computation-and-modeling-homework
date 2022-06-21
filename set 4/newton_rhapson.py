def func(x, n, num):
    return x ** n - num

def deriv(x, n):
    return n * x ** (n-1) 

def newton_rhapson(x, n, precision):
    x_old = 4
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

print(newton_rhapson(3, 2, .000000001))

def merge(a, b):
    result = []
    a_index = 0
    b_index = 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] > b[b_index]:
            result.append(b[b_index])
            b_index += 1
        else:
            result.append(a[a_index])
            a_index += 1
    if a_index < len(a):
        while a_index < len(a):
            result.append(a[a_index])
            a_index += 1
    else:
        while b_index < len(b):
            result.append(b[b_index])
            b_index += 1
    return result
