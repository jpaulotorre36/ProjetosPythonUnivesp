from random import randint
print("começo")
N = 0
while N < 10 or N > 10000:
    N = int(input("digite N entre [1, 10000]: "))
cod = []
cont = 0
while cont < N:
    a = randint(1000, 50000)
    if a not in cod:
        cod.append(a)
        cont += 1
S = "{0};{1};{2:.2f};{3}\n"
ICMS = (7, 12, 18)
arq = open("estoque.csv", "w")
cont = 0
while cont < N:
    Qtde = randint(1, 3800)
    PcUn = randint(180, 4390) / 100
    i = randint(0, 2)
    arq.write(S.format(cod[cont], Qtde, PcUn, ICMS[i]))
    cont += 1
arq.close()
print("fim")

