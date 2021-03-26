print("\nCálculo de estoque\n")
saida = "{:>7}{:>13.2f}{:>10.2f}{:>12.2f}"
TotICMS = 0
TotMerc = 0
print("Produto Val.Compra  ICMS Mercadoria")
arq = open("Estoque.csv", "r")
for s in arq.readlines():
      s = s.rstrip()
      L = s.split(";")
      L[0] = int(L[0])
      L[1] = int(L[1])
      L[2] = float(L[2])
      L[3] = float(L[3])/100
      compra = L[1] * L[2]
      icms = compra * L[3]
      merc = compra - icms
      TotICMS += icms
      TotMerc += merc
      print(saida.format(L[0], compra, icms, merc))
arq.close()
print(saida.format("Totais", TotMerc+TotICMS, TotICMS, TotMerc))
print("\n\nFim do Programa")
