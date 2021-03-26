def t(n):
    if n == 1:
       return 1

    else:
       return 2*t(n - 1) + 1


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fib(n - 1) + fib(n - 2)

    

   

    
