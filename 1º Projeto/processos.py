class Process:
    # Construtor
    def __init__(self, arrivalClock, firstRunClock, remainingClock, waitedClock, returnClock):
        self.arrivalClock = arrivalClock     # Tempo de chegada ao escalonador
        self.firstRunClock = firstRunClock   # Tempo da primeira execução na cpu
        self.remainingClock = remainingClock # Tempo restante de cpu
        self.waitedClock = waitedClock       # Tempo esperado na fila de espera
        self.returnClock = returnClock       # Tempo de saída apos completar a execução                

    #Tempo de resposta
    def get_responseClock(self):
        return self.firstRunClock - self.arrivalClock

    #Tempo de espera
    def get_waitedClock(self):
        return self.waitedClock

    #Tempo de retorno
    def get_returnClock(self):
        return self.returnClock - self.arrivalClock
