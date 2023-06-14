total_avaliacoes = int(input("Digite o total de avaliações: "))

soma_notas = 0

for _ in range(total_avaliacoes):
    nota = float(input("Digite a nota: "))
    soma_notas += nota

media = soma_notas / total_avaliacoes

print("A média aritmética das notas é:", media)
