#Esse codigo calculará as equações do segundo grau para você

import math

print("Bem Vindo a calculadora da Fórmula de Bhaskara")

valor_de_A = float(input("Informe o valor de A: "))
valor_de_B = float(input("Informe o valor de B: "))
valor_de_C = float(input("Informe o valor de C: "))

print(f"Equação: {valor_de_A}x² {valor_de_B}x e {valor_de_C} = 0")

valor_de_delta = (valor_de_B) ** 2 - 4 * valor_de_A * valor_de_C

if valor_de_delta > 0:
    #Calculo de X2 e X2
    X1 = (- valor_de_B + math.sqrt(valor_de_delta)) / (2 * valor_de_A)
    X2 = (- valor_de_B - math.sqrt(valor_de_delta)) / (2 * valor_de_A)
    print(f"O valor de X1 é: {X1}, já o de X2 é: {X2}")
elif valor_de_delta == 0:
    X = (- valor_de_B + math.sqrt(valor_de_delta)) / (2 * valor_de_A)
    print(f"O valor de x é: {X}")
else:
    print("Não existe valor para X.")