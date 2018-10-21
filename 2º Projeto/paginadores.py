''' paginadores (paginator) ''' 

def FIFO (pageList, memoryFrames):
    pages_inUse = [] #Lista de páginas em uso na RAM
    missingPages = 0 #Número de faltas de página

    #Quadros da memória são inciados com "vazio":
    for useless in range(memoryFrames):
        pages_inUse.append('empty')

    for page in pageList:
        #Incremento de falta de páginas:
        if(not page in pages_inUse):
            missingPages += 1

            ''' 
            A Substituição de páginas no padrão FIFO;
            a cada página não encontrada na memória:
            1 - Retira-se a primeira página dos quadros de memória
            2 - Adicionamos a pagina requerida no quadro recentemente aberto
            '''
            pages_inUse.pop(0)
            pages_inUse.append(page)

    return missingPages

def Otimo (pageList, memoryFrames):
    pages_inUse = [] #Lista de páginas em uso na RAM
    missingPages = 0 #Número de faltas de página
    i = 0            #Variável de comparação

    #Quadros da memória são inciados com "vazio":
    for useless in range(memoryFrames):
        pages_inUse.append('empty')
    
    for page in pageList:
        
        #Incremento de falta de páginas:
        if(not page in pages_inUse):
            missingPages += 1
            
            '''
            Substituição de páginas no padrão Ótimo:
            1 - Retira-se a página que mais demorará a ser referenciada.
            2 - Adicionamos a pagina requerida no quadro recentemente aberto.
            ''' 

            #Criando o indice de referências quando não houver mais espaços:        
            if(not 'empty' in pages_inUse):
                refIndex = []
                
                #Iniciando o indice de referências com nada:
                for useless in range(memoryFrames):
                    refIndex.append('nothing')

                page_inUse_index = 0 #Guarda o índice de referencia da página em uso

                #Verifica quando sera a próxima requisição das páginas que estão na RAM:
                for page_inUse in pages_inUse:

                    #Checa se a página é chamada na proxíma posição do indice de referências
                    if(page_inUse in pageList[i:]):
                        
                        #Se a pag for referenciada, vemos toda a lista para sabermos qual será sua posição:
                        for index in range(i, len(pageList)):
                        	#Encontrando, retiramos o parametro inicial e colocamos o valor encontrado.                             
                            if(page_inUse == pageList[index]):
                                refIndex[page_inUse_index] = index
                                break

                    page_inUse_index += 1 #incrementa a página em uso que está sendo verificada.
                
                #Se algum elemento não é mais chamado na lista:
                if('nothing' in refIndex):
                    pages_inUse.pop(refIndex.index('nothing')) #Retiramos o primeiro elemento que não for mais referenciado.
                    pages_inUse.append(page) #Adicionamos a página requisitada. 

                #Se não, verificamos qual a página que mais demorará a ser referenciada:
                else:
            		#A função max() pega o maior valor, ou seja o que mais demorará a ser  referenciado.
                    last_refIndex = refIndex.index(max(refIndex)) 

                    pages_inUse.pop(last_refIndex) #Retiramos a página que mais demorará a ser utilizada. 
                    pages_inUse.append(page) #Adicionamos a página requisitada.
            
            #Quando a inda se tem espaço é só adicionar no quadro vago.
            else:
                pages_inUse.pop(0) #"Retiramos" um empty. 
                pages_inUse.append(page) #Adiconamos o quadro requisitiado.

        i+= 1 #Incremento da váriavel auxiliar de comparação.
    
    return missingPages

def LRU (pageList, memoryFrames):
    pages_inUse = [] #Lista de páginas em uso na RAM
    missingPages = 0 #Número de faltas de página
    i = 0            #Variável de comparação

    #Quadros da memória são inciados com "vazio":
    for useless in range(memoryFrames):
        pages_inUse.append('empty')
    
    for page in pageList:
        
        #Incremento de falta de páginas:
        if(not page in pages_inUse):
            missingPages += 1
            
            '''
            Substituição de páginas no padrão Least Recently Used (LRU):
            1 - Retira-se a página que a mais tempo foi referenciada.
            2 - Adicionamos a pagina requerida no quadro recentemente aberto.
            ''' 

            #Criando o indice de referências quando não houver mais espaços:        
            if(not 'empty' in pages_inUse):
                refIndex = []
                
                #Iniciando o indice de referências com nada:
                for useless in range(memoryFrames):
                    refIndex.append('nothing')

                page_inUse_index = 0 #Guarda o índice de referencia da página em uso

                #Verifica quando sera a próxima requisição das páginas que estão na RAM:
                for page_inUse in pages_inUse:

                    #Checa se a página foi referenciada anteriormente.
                    if(page_inUse in pageList[0:i]):
                        
                        #Se a pag for referenciada, vemos toda a lista para sabermos qual será sua posição:
                        for index in range(0, i):
                        	#Encontrando, retiramos o parametro inicial e colocamos o valor encontrado.                             
                            if(page_inUse == pageList[index]):
                                refIndex[page_inUse_index] = index

                    page_inUse_index += 1 #incrementa a página em uso que está sendo verificada.
                	
                #Definimos o menos recentemente utilizado.
                lr_refIndex = refIndex.index(min(refIndex)) 

                pages_inUse.pop(lr_refIndex) #Retiramos a página que mais demorará a ser utilizada. 
                pages_inUse.append(page) #Adicionamos a página requisitada.
            
            #Quando a inda se tem espaço é só adicionar no quadro vago.
            else:
                pages_inUse.pop(0) #"Retiramos" um empty. 
                pages_inUse.append(page) #Adiconamos o quadro requisitiado.

        i+= 1 #Incremento da váriavel auxiliar de comparação.
    
    return missingPages