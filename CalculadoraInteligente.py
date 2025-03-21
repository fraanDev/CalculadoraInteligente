# Vamos começar printando para o usuário:
nome = input("Oi! Vamos começar. Como posso te chamar? Digite seu apelido: ")
print(f"Oi {nome}! Bem-vindx a calculadora inteligente. Em que posso te ajudar?")


#Inicio da calculadora - Criando uma função (calculadora)
def calculadora():
     #Começando o menu - Com um loop, para ter uma pausa quando o usuário decidir terminar
    while True:
        print("\n== MENU: ==")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
     #Criando uma variável - Pedindo uma resposta do usuário sobre as opções
        opcao = input("Escolha uma opção: ")
     #Opção de saída do menu - Utilizando o Break
        if opcao == "5":
            print("Saindo. Espero te ajudar mais na próxima. Até mais!")
            break
     #Caso o usuário escreva algo que não deveria, devolvemos:
        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Tente novamente.")
            continue
     # Respondendo o usuário caso ele escolha uma opção. float e input é atribuir a uma variavel, um valor decimal dado pelo usuario
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = num1 + num2
                operacao = "Adição"
            elif opcao == "2":
                resultado = num1 - num2
                operacao = "Subtração"
            elif opcao == "3":
                resultado = num1 * num2
                operacao = "Multiplicação"
            elif opcao == "4":
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
                operacao = "Divisão"
                
                   # Perguntar se o usuário quer arredondar o resultado
                arredondar = input("Deseja arredondar o resultado? (sim/nao): ").strip().lower()
                if arredondar == "sim":
                    casas_decimais = int(input("Quantas casas decimais deseja? "))
                    resultado = round(resultado, casas_decimais)

            print(f"\nResultado da {operacao}: {resultado}")

        except ValueError:
            print("Erro: Digite números válidos!")

calculadora()