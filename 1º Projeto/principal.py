''' Classe Principal '''
from processos import Process
import escalonador

processList_fcfs = []
processList_sjf = []
processList_rr = []

''' Solicitando a entrada: 
name = input("Informe o nome do arquivo que será executado: ")
with open('arquivos/{0}.txt'.format(name), 'r') as file_text:
'''

# Leitura do arquivo
with open('arquivos/teste.txt', 'r') as file_text:
    lines = file_text.read().splitlines()
    
    # Separamos para obter os tempos
    for line in lines:
        line = line.split()
        
        arrivalClock = int(line[0])   # 1º elemento da linha é o tempo de chegada 
        remainingClock = int(line[1]) # 2º elemento da linha é o tempo de cpu
         
        # Iniciamos a lista de Processos
        processList_fcfs.append(Process(arrivalClock, -1, remainingClock, 0, -1))
        processList_sjf.append(Process(arrivalClock, -1, remainingClock, 0, -1))
        processList_rr.append(Process(arrivalClock, -1, remainingClock, 0, -1))
        
#FCFS
processList_fcfs = escalonador.fcfs(processList_fcfs)


total_responseClock = 0
total_waitedClock = 0 
total_returnClock = 0

# Obtem o total dos tempos
for process in processList_fcfs:
    total_responseClock += process.get_responseClock()
    total_waitedClock += process.get_waitedClock()
    total_returnClock += process.get_returnClock()
    
# Calcula a media:
average_responseClock = total_responseClock/len(processList_fcfs)
average_waitedClock = total_waitedClock/len(processList_fcfs)
average_returnClock = total_returnClock/len(processList_fcfs)

# Exibe o resultado do escalonamento
print("FCFS ", "{0:0.1f}".format(average_returnClock), "{0:0.1f}".format(average_responseClock), "{0:0.1f}".format(average_waitedClock))

#SJF
processList_sjf = escalonador.sjf(processList_sjf)

total_responseClock = 0
total_waitedClock = 0 
total_returnClock = 0

for process in processList_sjf:
    total_responseClock += process.get_responseClock()
    total_waitedClock += process.get_waitedClock()
    total_returnClock += process.get_returnClock()

average_responseClock = total_responseClock/len(processList_fcfs)
average_waitedClock = total_waitedClock/len(processList_fcfs)
average_returnClock = total_returnClock/len(processList_fcfs)

print("SJF ", "{0:0.1f}".format(average_returnClock), "{0:0.1f}".format(average_responseClock), "{0:0.1f}".format(average_waitedClock))

#RR
processList_rr = escalonador.rr(processList_rr)

total_responseClock = 0
total_waitedClock = 0 
total_returnClock = 0

# Obtem o total dos tempos
for process in processList_rr:
    total_responseClock += process.get_responseClock()
    total_waitedClock += process.get_waitedClock()
    total_returnClock += process.get_returnClock()

# Calcula a media:
average_responseClock = total_responseClock/len(processList_fcfs)
average_waitedClock = total_waitedClock/len(processList_fcfs)
average_returnClock = total_returnClock/len(processList_fcfs)

print("RR ", "{0:0.1f}".format(average_returnClock), "{0:0.1f}".format(average_responseClock), "{0:0.1f}".format(average_waitedClock))