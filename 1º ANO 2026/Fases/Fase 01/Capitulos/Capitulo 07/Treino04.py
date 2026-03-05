# Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.

print("Votação para escolher o console a ser distribuido.")

console = [
    {'id': 1, 'nome': "PlayStation", 'votos': 0},
    {'id': 2, 'nome': "Xbox", 'votos': 0},
    {'id': 3, 'nome': "Nintendo", 'votos': 0},
]

votos = 0

for votos in range(5):
    add_votos = int(input(f"{votos + 1}/5 Adicione seu voto(1 - PlayStation, 2 - Xbox, 3 - Nintendo): "))
    match add_votos:
        case 1:
            print("Adicionando voto no PlayStation")
            console[0]['votos'] += 1
        case 2:
            print("Adicionando voto no Xbox")
            console[1]['votos'] += 1
        case 3:
            print("Adicionando voto no Nintendo")
            console[2]['votos'] += 1

maior = console[0]

for console in console:
    if console['votos'] > maior['votos']:
        maior = console

print()
print("Console vencedor:", maior['nome'])
print("Votos: ", maior['votos'])
