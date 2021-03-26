print("Início do Programa")
Soma = 0
Cont = 0
arq = open("Inteiros.txt", "r")
S = arq.readline()          
while S != '""\n':
    N =int(S)             
    Soma = Soma + N         
    Cont = Cont + 1         
    print("Elemento {0} = {1}".format(Cont, N))
    S = arq.readline()      
arq.close()
print("\nSoma = {0}".format(Soma))
print("Fim do Programa")
