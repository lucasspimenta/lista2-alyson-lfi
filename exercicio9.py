total_carros_ate_2000 = 0
total_geral = 0

while True:
    ano = int(input("Digite o ano do veículo: "))
    valor = float(input("Digite o valor do veículo: "))

    if ano <= 2000:
        desconto = valor * 0.12
        total_carros_ate_2000 += 1
    else:
        desconto = valor * 0.07

    valor_com_desconto = valor - desconto
    total_geral += valor_com_desconto

    print("Valor do desconto: R$", desconto)
    print("Valor a ser pago: R$", valor_com_desconto)

    opcao = input("Deseja continuar calculando desconto? (S/N): ")
    if opcao.upper() != "S":
        break

print("Total de carros com ano até 2000:", total_carros_ate_2000)
print("Total geral a ser pago pelos clientes: R$", total_geral)
