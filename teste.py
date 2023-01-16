from math import sqrt,trunc

num = 38

BigObject = {} 

count = trunc(sqrt(num + (num - 1)))

BigArray = [num, count ** 2 - num]

BigObject[count ** 2 - num] = count ** 2 - num
BigObject[num] = num

lado = True

numero = BigArray[-1]

contador = 0

def acharCompativeis(valor, lista, sizeContra):
    
    verificador = 0
    
    listaExcluidos = []
    
    for c in range(count, 1, -1):
        
        if (c ** 2) > valor:
            
            resultado = ((c ** 2) - valor) 
            
            resultado = resultado * -1 if resultado <= 0 else resultado
            
            
            if resultado <= num and resultado not in BigObject and valor != resultado:
                    
            
                if numero == BigArray[0] and sqrt(resultado + BigArray[-1]) % 1 == 0 or numero == BigArray[-1] and sqrt(resultado + BigArray[0]) % 1 == 0:

                    verificador = 1
                    
                    
                lista.append(resultado)
                        
                
                if sizeContra and sizeContra == 1:
                
                    if verificador == 1:
                        
                        listaExcluidos.append(lista[-1])
                        lista.pop()
                
                    
                verificador = 0
                

    sizeLista = len(lista)

    if sizeLista == 0 and len(listaExcluidos) > 0:
        
        lista += listaExcluidos
        
        
    elif sizeLista == 0:
        
        verificador = 2
        
    
    return verificador
        

while True:
    
    operaveis = []
    
    countOperaveis = {}
    
    numeroContra = BigArray[-1] if numero == BigArray[0] else BigArray[0]
    listaContra = []
    paresContra = acharCompativeis(numeroContra, listaContra, None)
    
    sizeContra = len(listaContra)

    sizeBigArray = len(BigArray)
    
    acharCompativeis(numero, operaveis, sizeContra)

    listaCandidatos = []
    
    soma = 0
    
    if len(operaveis) > 0:
        
        contador = 0
        
        for i in operaveis:
            
            countOperaveis[i] = []
            
            pares = acharCompativeis(i, countOperaveis[i], None)
            
            size = len(countOperaveis[i])
            
            if pares == 0 or pares == 2 and paresContra != 2 or sizeBigArray == num - 1:
                
                soma += size
                countOperaveis[i] = size
                
            else:
                
                del countOperaveis[i]

        escolhido = [*countOperaveis.values()]
        escolhido.sort()
        
        
        escolhido = [objeto for objeto in countOperaveis.keys() if countOperaveis[objeto] == escolhido[0]]
        
        escolhido = min(escolhido)
        
        
        BigArray.append(escolhido) if lado else BigArray.insert(0, escolhido)
        BigObject[escolhido] = operaveis
        
        print(escolhido)
        print(BigArray)
        
        listaDireita = []
        parDireita = acharCompativeis(BigArray[-1], listaDireita, None)
        sizeDireita = len(listaDireita)
        
        listaEsquerda = []
        parEsquerda = acharCompativeis(BigArray[0], listaEsquerda, None)
        sizeEsquerda = len(listaEsquerda)
        
        
        
        if soma == 0:
            if numero == BigArray[-2]:
                numero = BigArray[0]
            
                
            elif numero == BigArray[1]:
                numero = BigArray[-1]
        
        elif sizeDireita == sizeEsquerda:
            
            if numero == BigArray[-2]:
                numero = BigArray[-1]
            
                
            elif numero == BigArray[1]:
                numero = BigArray[0]
            
        else:
            if sizeDireita < sizeEsquerda:
                numero = BigArray[-1]
            

            elif sizeEsquerda < sizeDireita:
                numero = BigArray[0]
        
         
        
        lado = True if numero == BigArray[-1] else False
        
    else:
        
        lado = True if lado == False else False
        numero = BigArray[-1] if lado == True else BigArray[0]
        
        if contador == 2:
            
            print(False)
            exit()
            
        contador += 1
        
        
    if len(BigArray) == num:
        print(BigArray)
        break
    
    
    
            
        
        
        
        
        
        

