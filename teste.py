from math import sqrt,trunc

num = 39

BigObject = {} 

count = trunc(sqrt(num + (num - 1)))

BigArray = [num, count ** 2 - num]

BigObject[count ** 2 - num] = count ** 2 - num
BigObject[num] = num

lado = True

numero = BigArray[-1]

contador = 0

def acharCompativeis(valor, lista):
    
    for c in range(count, 1, -1):
        
        if (c ** 2) > valor:
            
            resultado = ((c ** 2) - valor) 
            
            resultado = resultado * -1 if resultado <= 0 else resultado
            
            
            if resultado <= num and resultado not in BigObject and valor != resultado:
                    
                    
                    
                lista.append(resultado)
                        
            
        


def retornarEscolhidos(valor):
    
    global numero
    global lado
    global contador
    
    operaveis = []
    
    countOperaveis = {}
    
    numeroContra = BigArray[-1] if numero == BigArray[0] else BigArray[0]
    listaContra = []
    acharCompativeis(numeroContra, listaContra)
    
    acharCompativeis(valor, operaveis)
    
    soma = 0
    
    if len(operaveis) > 0:
        
        contador = 0
        
        for i in operaveis:
            
            countOperaveis[i] = []
            
            acharCompativeis(i, countOperaveis[i])
            
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
        escolhido = retorno["escolhidos"]
        
        proximos = {}
        
        print(f"Numero: {numero}")
        print("escolhidos: ", escolhido)
        
        for c in escolhido:
            
            retornoProximos = retornarEscolhidos(c)
            
            print(f"{c} escolhidos(s): {retornoProximos['escolhidos'] if retornoProximos != None else 'None'}")
            
            
            
            proximos[len(retornoProximos["escolhidos"]) if retornoProximos != None else 0] = c
            
        escolhido = proximos[max(proximos.keys())] 
            
        soma = retorno["soma"]
            
        BigArray.append(escolhido) if lado else BigArray.insert(0, escolhido)
        
        BigObject[escolhido] = escolhido
        
        print(BigArray)
        
        listaDireita = []
        parDireita = acharCompativeis(BigArray[-1], listaDireita)
        sizeDireita = len(listaDireita)
        
        listaEsquerda = []
        parEsquerda = acharCompativeis(BigArray[0], listaEsquerda)
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
    
    
    if len(BigArray) == num:
        print(BigArray)
        break
    
    
    
            
        
        
        
        
        
        

