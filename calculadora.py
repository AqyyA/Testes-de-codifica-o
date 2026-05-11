def calculadora ():
    print ("==== calculadora ====")

    num1 = float (input ("digite seu primeiro numero:"))
    operacao = input ("digite a opereção que deseja +, _, *, /:")
    num2 = float (input ("digite seu segundo numero:"))

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
            print ("Erro: divisão por zero não é permitida.")
            return
        resultado = num1 / num2
    else:
        print ("Operação inválida.")
        return
    print (f"resultado: {num1} {operacao} {num2} = {resultado:.2f}")

calculadora ()
       
