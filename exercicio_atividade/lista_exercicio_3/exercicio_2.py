while True:
    usuario = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if senha != usuario:
        print("Cadastro realizado com sucesso.")
        break
    print("Erro: a senha não pode ser igual ao nome de usuário.")
