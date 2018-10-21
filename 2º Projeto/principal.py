''' Principal (MAIN) ''' 

import paginadores

#Criando a lista de páginas:
pageList = []

#Inicia a quantidade de quadros de memória:
memoryFrames = 0

#Abre o arquivo e separa-o em linhas e salvando-as em uma lista:
with open('arquivos/teste.txt', 'r') as file_text:
    lines = file_text.read().splitlines()

    #Flag para indentificar a primeira linha que é a quantidade de quadros disponiveis. 
    firstLine = -1

    for line in lines:
        #Define a quantidade de quadros de memória:
        if(firstLine == -1):
            memoryFrames = int(line)
            firstLine = 0

        #Enchemos a lista de páginas com as substituições informadas
        else:
            pageList.append(int(line))

#FIFO
missingPages = paginadores.FIFO(pageList, memoryFrames)
print("FIFO", missingPages)

#Ótimo
missingPages = paginadores.Otimo(pageList, memoryFrames)
print("OTM", missingPages)

#LRU
missingPages = paginadores.LRU(pageList, memoryFrames)
print("LRU", missingPages)
