from operator import mod


ano = int(input("Digite o ano para saber se é bissexto ou não: "))

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("O ano", ano , "é bissexto!")
else:
    print("Ano", ano ,  "não é bissexto")
