# Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos

valorBruto = float(input("Qual o valor do Bruto da viagem? "))
categoria = input("Qual a categoria da viagem? ").lower()
quantidadeDeViajantes = int(input("Quantos viajantes são? "))

#CATEGORIA ECONOMICA

if categoria == "economica":
    if quantidadeDeViajantes == 2:
        desconto = valorBruto * 0.03
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")
    elif quantidadeDeViajantes == 3:
        desconto = valorBruto * 0.04
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")
    elif quantidadeDeViajantes >= 4:
        desconto = valorBruto * 0.05
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")

#CATEGORIA EXECUTIVA

elif categoria == "executiva":
    if quantidadeDeViajantes == 2:
        desconto = valorBruto * 0.05
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")
    elif quantidadeDeViajantes == 3:
        desconto = valorBruto * 0.07
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")
    elif quantidadeDeViajantes >= 4:
        desconto = valorBruto * 0.08
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")

#CATEGORIA PRIMEIRA CLASSE

elif categoria == "primeira classe":
    if quantidadeDeViajantes == 2:
        desconto = valorBruto * 0.1
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")
    elif quantidadeDeViajantes == 3:
        desconto = valorBruto * 0.15
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")
    elif quantidadeDeViajantes >= 4:
        desconto = valorBruto * 0.2
        valorDescontado = valorBruto - desconto
        media = valorDescontado / quantidadeDeViajantes
        print(
            f"O valor da viagem {valorBruto}R$ com desconto de {desconto}R$ passará para {valorDescontado}R$, ficando numa média de {media:.2f}R$ por pessoa.")