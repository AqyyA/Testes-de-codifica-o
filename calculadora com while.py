def calculadora ():
    print ("==== calculadora ====")
    print ("Digite 'sair' para encerrar a calculadora.")

while True:
    entrada = input ("""
                    ==== calculadora ====
    Digite a operação (ex: 2 + 3) ou digite 'sair' para encerrar:""")


    if entrada.lower() == "sair":
        print ("encerrando")
        break
    try:
        partes = entrada.split()
        num1 = float (partes[0])
        operacao = partes[1]
        num2 = float (partes[2])
        
        
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
         resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print ("Erro: divisão por zero não é permitida.\n")
                continue
            resultado = num1 / num2 
        else: 
            print ("Operação inválida.\n")
            continue
        print (f" o resultado é: {resultado:.2f}\n")
    except (ValueError, IndexError):
        print("Formato invalido! Use: numero operacao\n")
calculadora()

 

          


    
    






