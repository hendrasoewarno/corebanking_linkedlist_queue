import time

class QueueAntrian():
    def __init__(self):
        self.queue=[]
        self.arrivalTime=[]
        self.calledTime=[]
        self.arrival=0
        self.called=0        
	
    def enQueue(self):
        self.arrival+=1
        self.queue.append(self.arrival)
        self.arrivalTime.append(time.time())
        return self.arrival
		
    def deQueue(self):
        if self.arrival > self.called:
            #FIFO
            queueNo=self.queue.pop(0)
            self.calledTime.append(time.time())
            self.called+=1
        return queueNo
    
    #waktu tunggu rata-rata diantrian
    def tQueue(self):
        if self.arrival==self.called:        
            return (sum(self.arrivalTime)-sum(self.calledTime))/self.arrival
        else:
            temp=self.calledTime+([time.time()]*(self.arrival-self.called))
            return (sum(temp)-sum(self.arrivalTime))/self.arrival
			
    #statistik antrian
    def statistic(self):
        print("Panjang antrian:", self.arrival-self.called)
        print("Total arrival:", self.arrival)
        print("Total called:", self.called)
        print("Waktu tunggu rata-rata:", self.tQueue(), "detik")