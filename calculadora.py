def realizar_operacoes(num1, num2):
    print("Operações com os números digitados:")
    print("Adição:", num1 + num2)
    print("Subtração:", num1 - num2)
    print("Multiplicação:", num1 * num2)
    print("Divisão:", num1 / num2)
    print("Divisão inteira:", num1 // num2)

    if num1 > num2:
        print("O primeiro número é maior que o segundo.")
    elif num1 < num2:
        print("O segundo número é maior que o primeiro.")
    else:
        print("Os números são iguais.")

while True:
    try:
        num = input("Digite o primeiro número para começar (ou 'sair' para encerrar): ")
        if num.lower() == 'sair':
            print("Encerrando o programa.")
            break
        num2 = input("Digite o segundo número: ")

        num_convert = int(num)
        num2_convert = int(num2)

        realizar_operacoes(num_convert, num2_convert)

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números.")

