from math import sqrt,trunc

num = 40

BigObject = {} 

count = trunc(sqrt(num + (num - 1)))

BigArray = [(count - 1) ** 2 - num, num, count ** 2 - num]
BigObject[(count - 1) ** 2 - num] = (count - 1) ** 2 - num
BigObject[count ** 2 - num] = count ** 2 - num
BigObject[num] = num

lado = True

verificador = True

numero = BigArray[-1]

def acharCompativeis(valor, lista):
    
    for c in range(count, 1, -1):
        
        global verificador
        
        if (c ** 2) > valor:
            
            resultado = ((c ** 2) - valor) 
            
            resultado = resultado * -1 if resultado <= 0 else resultado
            
            
            if resultado <= num and resultado not in BigObject and resultado != numero:
                    
                
                if valor == numero:
            
                    if numero == BigArray[0] and sqrt(resultado + BigArray[-1]) % 1 == 0 or numero == BigArray[-1] and sqrt(resultado + BigArray[0]) % 1 == 0:

                        verificador = True if verificador == False else False
                        
                        
                if verificador:    
                    
                    lista.append(resultado)
                
                    
                

                
                



while True:
    
    operaveis = []
    
    countOperaveis = {}
    
    acharCompativeis(numero, operaveis)

    listaCandidatos = []
    
    soma = 0
    
    if len(operaveis) > 0:
        
        for i in operaveis:
            
            countOperaveis[i] = []
            
            acharCompativeis(i, countOperaveis[i])
            
            size = len(countOperaveis[i])

            soma += size
            countOperaveis[i] = size
                

        escolhido = [*countOperaveis.values()]
        escolhido.sort()
        
        print(countOperaveis)
        
        escolhido = [objeto for objeto in countOperaveis.keys() if countOperaveis[objeto] == escolhido[0]][0]
        
        BigArray.append(escolhido) if lado else BigArray.insert(0, escolhido)
        BigObject[escolhido] = operaveis
        
        print(BigArray)
        
        if soma == 0 and numero == BigArray[-2]:
            numero = BigArray[0]
            lado = True
            
        elif soma == 0 and numero == BigArray[1]:
            numero = BigArray[-1]
            lado = False
            
            
        if soma != 0 and BigArray[-1] > BigArray[0]:
            numero = BigArray[-1]
            lado = True 
        elif soma != 0 and BigArray[0] > BigArray[-1]:
            numero = BigArray[0]
            lado = False
        
    else:
        
        lado = True if lado == False else False
        numero = BigArray[-1] if lado == True else BigArray[0]
        
        
    if len(BigArray) == num:
        break
    
    
    
            
        
        
        
        
        
        

