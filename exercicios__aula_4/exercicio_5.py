opcoes_validas = ["sol", "chuva", "nublado"]

previsao_mensagem = input("Digite a previsão do tempo (sol, chuva ou nublado): ").lower()

def validar_previsao(previsao):
    while previsao not in opcoes_validas:
        print("Opção inválida. Tente novamente.")
        previsao = input("Digite a previsão do tempo (sol, chuva ou nublado): ").lower()
    return previsao


def mostrar_mensagem(previsao):
    if previsao == "sol":
        print("Não esqueça o filtro solar")
    elif previsao == "chuva":
        print("Use guarda-chuva")
    elif previsao == "nublado":
        print("O tempo está ótimo")


previsao = validar_previsao(previsao_mensagem)
mostrar_mensagem(previsao)