import sys

# 1 litro de Etanol = 0.70 de Gasolina

gasolina = float(input("Informe o preço da Gasolina: "))
etanol = float(input("Informe o preço do Etanol: "))


if (gasolina * 0.70) <= etanol:
    print("É melhor abastecer com Gasolina, amigo.")
else:
    print("O Etanol tá compensando!")    


