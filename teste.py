from math import sqrt,trunc

num = 23

BigObject = {} 

count = trunc(sqrt(num + (num - 1)))

BigArray = [num, count ** 2 - num]

BigObject[count ** 2 - num] = count ** 2 - num
BigObject[num] = num

lado = True

numero = BigArray[-1]

def acharCompativeis(valor, lista):
    
    verificador = 0
    
    for c in range(count, 1, -1):
        
        if (c ** 2) > valor:
            
            resultado = ((c ** 2) - valor) 
            
            resultado = resultado * -1 if resultado <= 0 else resultado
            
            
            if resultado <= num and resultado not in BigObject and valor != resultado:
                    
            
                if numero == BigArray[0] and sqrt(resultado + BigArray[-1]) % 1 == 0 or numero == BigArray[-1] and sqrt(resultado + BigArray[0]) % 1 == 0:

                    verificador = 1
                        
                
                lista.append(resultado)
                

    sizeLista = len(lista)

    if sizeLista == 0:
        
        verificador = 2
        
    
    return verificador
        

while True:
    
    operaveis = []
    
    countOperaveis = {}
    
    acharCompativeis(numero, operaveis)

    listaCandidatos = []
    
    soma = 0
    
    if len(operaveis) > 0:
        
        numeroContra = BigArray[-1] if numero == BigArray[0] else BigArray[0]
        listaContra = []
        paresContra = acharCompativeis(numeroContra, listaContra)
        
        sizeContra = len(listaContra)

        sizeBigArray = len(BigArray)
        
        for i in operaveis:
            
            countOperaveis[i] = []
            
            pares = acharCompativeis(i, countOperaveis[i])
            
            size = len(countOperaveis[i])
        
            
            
            soma += size
            countOperaveis[i] = size

         
            
        escolhido = [*countOperaveis.values()]
        escolhido.sort()
        
        print(countOperaveis)
        
        try :
            escolhido = [objeto for objeto in countOperaveis.keys() if countOperaveis[objeto] == escolhido[0]][0]
        except:
            print(False)
        
        BigArray.append(escolhido) if lado else BigArray.insert(0, escolhido)
        BigObject[escolhido] = operaveis
        
        print(BigArray)
        
        listaDireita = []
        parDireita = acharCompativeis(BigArray[-1], listaDireita)
        sizeDireita = len(listaDireita)
        
        listaEsquerda = []
        parEsquerda = acharCompativeis(BigArray[0], listaEsquerda)
        sizeEsquerda = len(listaEsquerda)
        
        
        if soma == 0 and numero == BigArray[-2]:
            numero = BigArray[0]
          
            
        elif soma == 0 and numero == BigArray[1]:
            numero = BigArray[-1]
            
         
            
        if soma != 0 and sizeDireita < sizeEsquerda or BigArray[-1] > BigArray[0]:
            
            numero = BigArray[-1]
           

        elif soma != 0 and sizeEsquerda < sizeDireita or BigArray[0] > BigArray[-1]:
            
            numero = BigArray[0]
        
         
        
        lado = True if numero == BigArray[-1] else False
        
    else:
        
        lado = True if lado == False else False
        numero = BigArray[-1] if lado == True else BigArray[0]
        
        
    if len(BigArray) == num:
        break
    
    
    
            
        
        
        
        
        
        

