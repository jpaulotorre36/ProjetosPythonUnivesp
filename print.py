

def taxasC(n):
    'mostra valores para3 funções usando i = 1,...,n'
    print('i', 'i**2', 'i**3', '2**i')
    format_str = '{0:2d} {1:6d} {2:6d} {3:6d}'
    for i in range (2, n+1):
        print(format_str.format(1, 1**2, 1**3, 2**1))

n = eval(input('digite n:'))

    
