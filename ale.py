
import random

print("Olá tudo bem?")
print("Vamos ver se você encontra algum valor da nossa lista de 4 números")



rresultado = random.sample(range(0, 100), 4)

while (n not in resultado):
    
    n = int(input("Digite um número interio mairo do que 0 e menor do que 100: "))
    
    if n in resultado:
        print("Parabéns você digitou um número valido")     
    

    else:
        print("Você errou")
    


print(resultado)
    

