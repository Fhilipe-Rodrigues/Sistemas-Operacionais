''' Escalonadores '''
from processos import Process

# função usada usada como parâmetro para a ordenação por tempo de cpu
def processSort_remainingClock(process):
          return process.remainingClock

# Escalonador do tipo FCFS
def fcfs(processList):
    clock = 0		  # Ciclo
    maxClock = 0 	  # Máximo de ciclos
    run = [] 		  # Lista de processos rodando
    waiting = [] 	  # Fila de espera
    completedProcess = [] # Lista de processos completados.

    # Pegamos o tempo máximo de ciclos para utilizarmos como condição de parada
    for process in processList:
    	maxClock += process.remainingClock

    while(clock <= maxClock):
        
        for i in range(len(processList)):
            # Organiza a fila de acordo com a ordem de chegada
            if(processList[i].arrivalClock == clock):
                # .append adiciona o elemento no final da lista
                waiting.append(Process(processList[i].arrivalClock, processList[i].firstRunClock,
                                       processList[i].remainingClock, processList[i].waitedClock, processList[i].returnClock))
                
        #removendo o processo da execução
        if (len(run) != 0 and run[0].remainingClock == 0):
            run[0].returnClock = clock
            completedProcess.append(run.pop())

        # Colocando o processo para rodar
        if(len(run) == 0 and len(waiting) != 0):
            
            # Processo da  fila de espera vai para lista de execução
            run.append(waiting.pop(0))
            
            # Os processos começam com o tempo de inicio -1
            # como uma flag para podermos setar o clock em que ele começou a rodar.
            if(run[0].firstRunClock == -1):
                run[0].firstRunClock = clock
            
        # Ajustes de ciclo
        
        # Incremeto do tempo de espera
        for i in range(len(waiting)):
            waiting[i].waitedClock += 1

        # Decremento do tempo de cpu
        if(len(run) != 0):
            run[0].remainingClock -= 1

        # Incremento de ciclo
        clock += 1
    
    #Retorna a lista dos processos completados.
    return completedProcess
     
# Escalonador do tipo SJF
def sjf(processList):
    clock = 0		  # Ciclo
    maxClock = 0 	  # Máximo de ciclos
    run = [] 		  # Lista de processos rodando
    waiting = [] 	  # Fila de espera
    completedProcess = [] # Lista de processos completados.
    
    # Pegamos o tempo máximo de ciclos para utilizarmos como condição de parada
    for process in processList:
    	maxClock += process.remainingClock

    while(clock <= maxClock):
        for i in range(len(processList)):
        	# Organiza a fila de acordo com a ordem de chegada
	        if(processList[i].arrivalClock == clock):
	            # .append adiciona o elemento no final da lista
	            waiting.append(Process(processList[i].arrivalClock, processList[i].firstRunClock,
	                                   processList[i].remainingClock, processList[i].waitedClock, processList[i].returnClock))

	            # sorted organiza a fila de espera de acordo com o tamanho do tempo de cpu
	            waiting = sorted(waiting, key = processSort_remainingClock)
				
		#removendo o processo da execução
        if (len(run) != 0 and run[0].remainingClock == 0):
            run[0].returnClock = clock
            completedProcess.append(run.pop())

        # Colocando o processo para rodar
        if(len(run) == 0 and len(waiting) != 0):
        	
        	# Processo da  fila de espera vai para lista de execução
            run.append(waiting.pop(0))
			
			# Os processos começam com o tempo de inicio -1
            # como uma flag para podermos setar o clock em que ele começou a rodar.            	
            if(run[0].firstRunClock == -1):
            	run[0].firstRunClock = clock

        # Ajustes de ciclo
        
        # Incremeto do tempo de espera
        for i in range(len(waiting)):
            waiting[i].waitedClock += 1

        # Decremento do tempo de cpu
        if(len(run) != 0):
            run[0].remainingClock -= 1

        # Incremento de ciclo
        clock += 1
    
    #Retorna a lista dos processos completados.
    return completedProcess

# Escalonador do tipo RR
def rr(processList):
    q = 2 			  # Váriavel local que define o número máximo de ciclos
    quantum = q       # Quantidade máximas de ciclo que o processo pode executar.
    clock = 0		  # Ciclo
    maxClock = 0 	  # Máximo de ciclos
    run = [] 		  # Lista de processos rodando
    waiting = [] 	  # Fila de espera
    completedProcess = [] # Lista de processos completados.
    
    # Pegamos o tempo máximo de ciclos para utilizarmos como condição de parada
    for process in processList:
    	maxClock += process.remainingClock

    while(clock <= maxClock):
        for i in range(len(processList)):
        	# Organiza a fila de acordo com a ordem de chegada
	        if(processList[i].arrivalClock == clock):
	            # .append adiciona o elemento no final da lista
	            waiting.append(Process(processList[i].arrivalClock, processList[i].firstRunClock,
	                                    processList[i].remainingClock, processList[i].waitedClock, processList[i].returnClock))

	    # Remoção caso 1:
	    # Processo está rodando, e seu tempo de cpu acabou
        if (len(run) != 0 and run[0].remainingClock == 0):
 
            # Seta o tempo de retorno e envia o processo para a fila de completados
            run[0].returnClock = clock
            completedProcess.append(run.pop())

            # Reinicia o tempo de quantum:
            quantum = q
            
           
        # Remoção caso 2: 
        # Processo está rodando, e seu tempo de quantum acabou
        if (len(run) != 0 and quantum == 0):

        	# O processo vai para a fila de espera
        	waiting.append(run.pop())

        	# Reinicia o tempo de quantum:
        	quantum = q


        # Colocando o processo para rodar
        if(len(run) == 0 and len(waiting) != 0):
        	
        	# Processo da  fila de espera vai para lista de execução
            run.append(waiting.pop(0))
			
			# Os processos começam com o tempo de inicio -1
            # como uma flag para podermos setar o clock em que ele começou a rodar.            	
            if(run[0].firstRunClock == -1):
            	run[0].firstRunClock = clock
        
        # Ajustes de ciclo
        
        # Incremeto do tempo de espera
        for i in range(len(waiting)):
            waiting[i].waitedClock += 1

        # Decremento do tempo de cpu e quantum
        if(len(run) != 0):
            run[0].remainingClock -= 1
            quantum -= 1 

        # Incremento de ciclo
        clock += 1
    
    #Retorna a lista dos processos completados.
    return completedProcess



