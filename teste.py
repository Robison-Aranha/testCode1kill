from math import sqrt,trunc

num = 40

BigObject = {} 
DispoObject = {}

count = trunc(sqrt(num + (num - 1)))

BigArray = [num, count ** 2 - num]

BigObject[count ** 2 - num] = count ** 2 - num 
BigObject[num] = num

lado = True

numero = BigArray[-1]

contador = 0

arrayResrtrito = []

def acharCompativeis(valor, lista, verificador):
    
    for c in range(count, 1, -1):
        
        if (c ** 2) > valor:
            
            resultado = ((c ** 2) - valor) 
            
            resultado = resultado * -1 if resultado <= 0 else resultado
            
            valorContra = BigArray[-1] if numero == BigArray[0] else BigArray[0]
            
            if resultado <= num and valor != resultado and resultado not in arrayResrtrito:
                
                if resultado not in BigObject or verificador != None and resultado == valorContra:
                    
                    lista.append(resultado)
                        

def acharEscolhido(lista):
    
    keymap = {}
    dictValores = {}
    menorValor = -1
    
    global arrayResrtrito
    
    while True:
    
        arrayResrtrito += lista[:]
        
        for i in lista:
            
            retorno = retornarEscolhidos(i)
                
            keymap[i] = retorno["escolhidos"]
            
            for h in retorno["escolhidos"]:
                
                listaEscolhido = []
                acharCompativeis(h, listaEscolhido, True)
                
                size = len(listaEscolhido)
                keymap[h] = size
                dictValores[h] = i
                
                if menorValor == -1:
                    
                    menorValor = size
                    
                elif size < menorValor:
                    
                    menorValor = size
                        
            
                    
        
        listaMenor = []
        
        for c in lista:
            
            lista2 = []
            
            for i in keymap[c]:
                
                lista2.append(keymap[i])
                
            listaMenor.append(min(lista2))
                
        
        listaNova = []
            
        for i in lista:
            
            for h in keymap[i]:
                
                if menorValor == keymap[h]:
                    
                    if listaMenor.count(menorValor) == 1:  
                        
                        key = h
                        
                        try:
                            
                            key = dictValores[key]
                            
                        except:
                            
                            return key
                            
                    
                    listaNova.append(h)
                    
        
        lista = listaNova[:]
            
            


def retornarEscolhidos(valor):
    
    global numero
    global lado
    global contador
    
    operaveis = []
    
    countOperaveis = {}
    
    acharCompativeis(valor, operaveis, None)
    
    soma = 0
    
    if len(operaveis) > 0:
        
        contador = 0
        
        for i in operaveis:
            
            
            countOperaveis[i] = []
            
            acharCompativeis(i, countOperaveis[i], True)
            
            size = len(countOperaveis[i])
            
            soma += size
            countOperaveis[i] = size
            
                
           
        escolhido = [*countOperaveis.values()]
        escolhido.sort()
        
        
        escolhido = [objeto for objeto in countOperaveis.keys() if countOperaveis[objeto] == escolhido[0]]
        
        
        return {"escolhidos": escolhido, "soma": soma}
    

while True:

    retorno = retornarEscolhidos(numero)
    
    if retorno == None:
        
        lado = True if lado == False else False
        numero = BigArray[-1] if lado == True else BigArray[0]
    
        if contador == 2:
            
            print(False)
            exit()
        
        contador += 1
    
    else:
        
        contador = 0
        
        escolhido = retorno["escolhidos"]  
        
        print(f"Numero: {numero}")
        print("escolhidos: ", escolhido)
        
        if len(escolhido) > 1:
            
            escolhido = acharEscolhido(escolhido)
            
            arrayResrtrito = []
        
        else:
            
            escolhido = escolhido[0]
        
        soma = retorno["soma"]
            
        BigArray.append(escolhido) if lado else BigArray.insert(0, escolhido)
        
        BigObject[escolhido] = escolhido
        
        listaDireita = []
        parDireita = acharCompativeis(BigArray[-1], listaDireita, None)
        sizeDireita = len(listaDireita)
        
        listaEsquerda = []
        parEsquerda = acharCompativeis(BigArray[0], listaEsquerda, None)
        sizeEsquerda = len(listaEsquerda)
        
        print(f"sizeDireita: {sizeDireita}")
        print(f"sizeEsquerda: {sizeEsquerda}")
        
        print(BigArray)
        
        if soma == 0:
            if numero == BigArray[-2]:
                numero = BigArray[0]
            
                
            elif numero == BigArray[1]:
                numero = BigArray[-1]
                
        elif sizeDireita == sizeEsquerda:
            
            numero = acharEscolhido([BigArray[0], BigArray[-1]])
            
            arrayResrtrito = []
        
        else:
            
            if sizeEsquerda > sizeDireita:
                numero = BigArray[-1]
            

            elif sizeDireita > sizeEsquerda:
                numero = BigArray[0]
        
        
        
        lado = True if numero == BigArray[-1] else False
    
    
    if len(BigArray) == num:
        print(BigArray)
        break
    
    
    
            
        
        
        
        
        
        

