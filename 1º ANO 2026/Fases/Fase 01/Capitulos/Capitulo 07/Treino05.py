#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.

print("Calcular valor de bônus:")

print()

print("Selecione o tipo de assinatura:")
print("Basic")
print("Silver")
print("Gold")
print("Platinum")

print()


tipo_assinatura = input("Selecione o tipo de assinatura: ").lower()
faturamento_anual = float(input("Informe seu faturamento anual: "))

match tipo_assinatura:
    case "basic":
        bonus = faturamento_anual * 0.3
        print(f"Plano {tipo_assinatura.upper()}")
        print(f"O bônus a ser pago é: {bonus:.2f}")
    case "silver":
        bonus = faturamento_anual * 0.2
        print(f"Plano {tipo_assinatura.upper()}")
        print(f"O bônus a ser pago é: {bonus:.2f}")
    case "gold":
        bonus = faturamento_anual * 0.1
        print(f"Plano {tipo_assinatura.upper()}")
        print(f"O bônus a ser pago é: {bonus:.2f}")
    case "platinum":
        bonus = faturamento_anual * 0.05
        print(f"Plano {tipo_assinatura.upper()}")
        print(f"O bônus a ser pago é: {bonus:.2f}")