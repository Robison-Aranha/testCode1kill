from math import sqrt,trunc

num = 23

BigObject = {} 
BigArray = [num]

count = trunc(sqrt(num + (num - 1)))

numero = num

def acharCompativeis(valor, lista):
    
    for c in range(count, 0, -1):
        
        resultado = ((c ** 2) - valor) 
        
        resultado = resultado * -1 if resultado < 0 else resultado
        
        if resultado <= num and BigObject[resultado] == None:
        
            lista.append(resultado)
            BigObject[resultado] = resultado


while True:
    
    lado = -1
    
    contador = count
    
    operaveis = []
    
    countOperaveis = {}
    
    acharCompativeis(numero, operaveis)
    
    listaCandidatos = []
    
    soma = 0
    
    for i in operaveis:
        
        countOperaveis[i] = []
        
        acharCompativeis(i, countOperaveis[i])
        
        if len(countOperaveis[i]) > 0:
            soma += len(countOperaveis[i])
            countOperaveis[len(countOperaveis[i])] = i
            listaCandidatos.append(len(countOperaveis[i]))
        
    listaCandidatos.sort()
    
    lado = -1 if soma > 0 else 0
    
    BigArray.insert(lado, countOperaveis[listaCandidatos[0]])
    
    if len(BigArray) == num:
        break
    
    
    
            
        
        
        
        
        
        

