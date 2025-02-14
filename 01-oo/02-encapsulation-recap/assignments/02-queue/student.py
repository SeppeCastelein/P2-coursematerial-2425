class Queue:
    def __init__ (self):
        self.queue = []
        
    def add(self, item):
        self.queue.append(item)

    def next(self):
        if self.queue:
            return self.queue.pop(0) 
        else:
            return None
        
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return None
        
queue = Queue()

queue.add('Alice')
queue.add('Bob')
queue.add('Charlie')

queue.next()