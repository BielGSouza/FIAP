# Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.

BPM = int(input("Informe seu BPM: "))
Idade = int(input("Informe sua idade: "))

if Idade <= 2:
    if BPM < 120:
        print("Batimentos ABAIXO do esperado.")
    elif 120 <= BPM <= 140:
        print("Batimentos DENTRO da faixa adequada.")
    else:
        print("Batimentos ACIMA do esperado")
elif 8 <= Idade <= 17:
    if BPM < 80:
        print("Batimentos ABAIXO do esperado.")
    elif 80 <= BPM <= 100:
        print("Batimentos DENTRO da faixa adequada.")
    else:
        print("Batimentos ACIMA do esperado")
elif 18 <= Idade <= 50:
    if BPM < 70:
        print("Batimentos ABAIXO do esperado.")
    elif 70 <= BPM <= 80:
        print("Batimentos DENTRO da faixa adequada.")
    else:
        print("Batimentos ACIMA do esperado")
elif 51 <= Idade:
    if BPM < 50:
        print("Batimentos ABAIXO do esperado.")
    elif 50 <= BPM <= 60:
        print("Batimentos DENTRO da faixa adequada.")
    else:
        print("Batimentos ACIMA do esperado")
else:
    print("Não constamos sua idade na tabela")
