import queue as q

'''
Traverse on a graph
If graph is weighted, ignores weights while traversing
'''
class Traverse:
    def __init__(self,graph):
        self.graph = graph
        self.visited = []

    def __str__(self):
        return self.visited.__str__()
    
    def startBFS(self,sourceId):
        self.visited = []
        queue = q.Queue()
        self.source = self.graph.getVertex(sourceId)
        queue._put(self.source)
        
        '''DEQUEUE THE QUEUE ITEMS UNTIL EMPTY'''
        while (queue.empty() is not True):
            current = queue.get()
            if(current.getId() not in self.visited):
                self.visited.append(current.getId())
                for neighbor in current.getOutNeighbors():
                    if(neighbor.getId() not in self.visited):
                        queue.put(neighbor)
        return self
        
    def startDFS(self,sourceId):
        self.visited = []
        stack = []
        self.source = self.graph.getVertex(sourceId)
        stack.append(self.source)
        
        '''POP THE STACK ITEMS UNTIL EMPTY'''
        while (stack):
            current = stack.pop()
            if(current.getId() not in self.visited):
                self.visited.append(current.getId())
                for neighbor in current.getOutNeighbors():
                    if(neighbor.getId() not in self.visited):
                        stack.append(neighbor)
        return self