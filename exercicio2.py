while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if senha != nome_usuario:
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")
        
print("Nome de usuário:", nome_usuario)
print("Senha:", senha)
