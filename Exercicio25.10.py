def f(a,p):
    """Função para calcular IMC"""
    return p /(a ** 2)

p = int(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

print("Seu IMC é: ")
#print(f(a,p))
print("%.2f" % f(a,p)) #Limitando a quantidade de casas decimais (2 casas)