#Esse codigo verifica se o cupom digitado é valdo no desconto da sua compra

cupom = input("Qual o cupom de desconto: ").upper()
nome_da_peca = input("Qual o nome da peca de adquirida: ")
valor_da_peca = float(input("Qual o valor da peca de adquirida: "))
desconto_da_peca = valor_da_peca - (valor_da_peca * 0.1)

if cupom == "NIVER10":
    print(f"Cupom {cupom} válido...")
    print("Aplicando desconto...")
    print(f"O valor da sua peça {nome_da_peca} ficou de {valor_da_peca} para {desconto_da_peca}")
else:
    print("Cupom inválido! Tente novamente.")