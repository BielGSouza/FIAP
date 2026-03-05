#Esse codigo verifica com uso dos if simpels se voce esta dentro da expediçao ou nao, caso tire a nota superior que 8,5
print("Veja se você fará parte da expedição para a America do Sul")

email = input("Digite seu e-mail: ")
nota = float(input("Digite sua nota: "))

if nota >= 8.5:
    print("PARABENS, você fará parte da nossa expedição para a America do Sul!")
    print("EVIANDO CONVITE para {}.".format(email))