"""
Escreva um programa que lê um número n
 maior que 1 e imprime a decomposição desse número em fatores primos. O formato é como mostramos a seguir:

Exemplos:

Entrada: 12

Saída: 2 ^ 2 * 3 ^ 1 (2 elevado a 2 vezes 3 elevado a 1)

Entrada: 50

Saída:  2 ^ 1 * 5 ^ 2 (2 elevado a 1 vezes 5 elevado a 2)
"""
n = int(input(""))
dividendo = 2
div = 1
primo = 0  
i = 0
apresentacao = ""
potencia = 0

if n > 1:
    while n != 1:
        if n % dividendo == 0:
            base = dividendo
            potencia +=1 
            n = n // dividendo
        else:
            if apresentacao == "":
                apresentacao = str(base)+"^"+str(potencia)
            else:    
                apresentacao = apresentacao +" * "+ str(base)+" ^ "+str(potencia)

            dividendo +=1
            while div != dividendo:
                div +=1                
                if dividendo % div == 0:
                    primo +=1                                        
                
                if primo > 2:
                    dividendo +=1 
                    div == 1

if apresentacao == "":
    apresentacao = str(base)+" ^ "+str(potencia)
else:    
    apresentacao = apresentacao +" * "+ str(base)+" ^ "+str(potencia)                
print(apresentacao)