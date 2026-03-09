import heapq

def astrk(graph,start,goal,h) : # -- h represnrt huristic 
    pq = [(h[start],0,[start])]
    visited = set()

    while pq:
        f,g,current,path = heapq.heappop(pq)


        if current == goal :
            return path 
        
        if current not in visited :
            visited.add(current)
        
        for neighbour,weight in graph(current) :
            new_g = g + weight
            new_f = new_g + h[neighbour]
            heapq.heappush(pq,(new_f,new_g,neighbour,path +[neighbour]))
    return None