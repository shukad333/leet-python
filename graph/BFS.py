from collections import defaultdict
class BFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        #print (len(self.graph))
        visited = [False] * (len(self.graph)+1)
        #print(visited)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s=queue.pop(0)
            print(s)

            for i in self.graph[s]:
                #print("i is ",i)
                if visited[i]==False:
                    queue.append(i)
                    visited[i] = True
g = BFS()
g.addEdge(1,3)
g.addEdge(2,1)
g.addEdge(3,1)
g.addEdge(1,2)
g.BFS(1)

