sair = False
while not sair:
    num1 = float(input("Digite o primeiro   número\n"))
    num2 = float(input("Digite o segundo    número\n"))
    operador = input("Digite o operador     desejado\n[+] para adição\n[-] para     subtração\n[/] para divisão\n[*] para   multiplicação\n")
    if operador == '+':
        resultado = (num1 + num2)
        print(f"A soma de {num1} + {num2} é igual a {resultado:.2f}\n")
    elif operador == '-':
        resultado = (num1 - num2)
        print(f"A subtração de {num1}-  {num2} é igual a {resultado:.2f}\n")
    elif operador == '/':
        resultado = (num1 / num2)
        print(f"A divisão de {num1} / {num2} é igual a {resultado:.2f}\n")
    elif operador == '*':
        resultado = (num1 * num2)
        print(f"A multiplicação de {num1} * {num2} é igual a {resultado:.2f}\n")
    else:
        print("Opção inválida\n")
    sair = input("Digite [s] para sair:\nOu pressione qualquer tecla para continuar na calculadora").lower().startswith('s')