while True:
    numero_aluno = input("Digite o número de identificação do aluno: ")
    nota1 = float(input("Digite a primeira nota (entre 0 e 10): "))
    nota2 = float(input("Digite a segunda nota (entre 0 e 10): "))
    nota3 = float(input("Digite a terceira nota (entre 0 e 10): "))
    nota_exercicios = float(input("Digite a nota dos exercícios (entre 0 e 10): "))
    
    media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + nota_exercicios) / 7
    
    conceito = ""
    if media_aproveitamento >= 9.0:
        conceito = "A"
    elif media_aproveitamento >= 7.5:
        conceito = "B"
    elif media_aproveitamento >= 6.0:
        conceito = "C"
    elif media_aproveitamento >= 4.0:
        conceito = "D"
    else:
        conceito = "E"
        
    print("\nNúmero do aluno:", numero_aluno)
    print("Notas: ", nota1, nota2, nota3)
    print("Média dos exercícios:", nota_exercicios)
    print("Média de aproveitamento:", media_aproveitamento)
    print("Conceito:", conceito)
    
    if conceito == "A" or conceito == "B" or conceito == "C":
        print("APROVADO\n")
    else:
        print("REPROVADO\n")
    
    opcao = input("Deseja digitar as notas de outro aluno? (S/N): ")
    if opcao.upper() != "S":
        break
