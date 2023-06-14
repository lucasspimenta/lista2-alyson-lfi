for i in range(1, 76):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
