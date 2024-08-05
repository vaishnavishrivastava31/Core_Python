import queue


class Queue:
    def __init__(self,size):
        self.size=size
        self.front=0
        self.rear=-1
        self.count=0
        self.queue = [None]*size

    def is_Empty(self):
        return self.count == 0
    def is_Full(self):
        return self.count == self.size
    def enqueue(self,item):
        if self.is_Full():
            print('Queue is full')
            return
        self.rear = (self.rear+1)%self.size
        self.queue[self.rear]=item
        self.count+=1
    def dequeue(self):
        if self.is_Empty():
            print('Queue is empty')
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front+1)%self.size
        self.count-=1
        return item
    def display(self):
        if self.is_Empty():
            print('Queue is empty')
        else:
            index = self.front
            items = []
            for _ in range(0,self.count):
                items.append(self.queue[index])
                index = (index+1)%self.size
            print("Queue", items)

q=Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
print(q.dequeue())
q.display()