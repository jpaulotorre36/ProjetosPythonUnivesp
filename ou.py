def Soma(x,y):
    r = x + y
    return r
a = int(input('valor para a: '))

b = int(input('valor para b: '))

c = int(input('valor para c: '))

s = soma(a,b)
print('a + b = {0}'.format(s))

s = soma(a,c)
print('a + c = {0}'.format(s))
