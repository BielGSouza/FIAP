#Atividade da Live de Python

salarioBruto = float(input("Informe o seu salário: "))
salarioComINSS = 0

#Calculo de deconto da tabela do INSS segundo o GOV

if salarioBruto < 1621:
    descontoINSS = salarioBruto * 0.075
    salarioComINSS = salarioBruto - descontoINSS
elif 1621.01 < salarioBruto < 2902.84:
    descontoINSS = salarioBruto * 0.09
    salarioComINSS = salarioBruto - descontoINSS
elif 2902.85 < salarioBruto < 4354.27:
    descontoINSS = salarioBruto * 0.12
    salarioComINSS = salarioBruto - descontoINSS
elif 4354.28 < salarioBruto < 8475.55:
    descontoINSS = salarioBruto * 0.14
    salarioComINSS = salarioBruto - descontoINSS

#Calculo do  desconto do IR sengundo o GOV

if salarioBruto < 2428.80:
    descontoIR = 0
elif 2428.81 < salarioBruto < 2826.65:
    descontoIR = salarioBruto * 0.075
elif 2826.66 < salarioBruto < 3751.05:
    descontoIR = salarioBruto * 0.15
elif 3751.06 < salarioBruto < 4664.68:
    descontoIR = salarioBruto * 0.225
elif salarioBruto > 4646.69:
    descontoIR = salarioBruto * 0.275

print(f"""
    Salário Bruto:                      {salarioBruto:.2f}
    Valor do desconto do INSS:          {descontoINSS:.2f} 
    Valor do desconto IR:               {descontoIR}
    Salário liquido:                    {salarioBruto - descontoIR - descontoINSS:.2f}
""")