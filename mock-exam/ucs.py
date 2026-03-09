import heapq 

def ucs(graph,start,goal) :
    pq = [(0,start,[start])] # -- (Cost,node,path)

    visited  =  set()
    

    while pq :
        cost,current,path = heapq.heappop(pq) #-- sb se kam cost return kare ga

        if current == goal :
            return path,cost
        
        if current not in visited :
            visited.add(current)

        for neighbour ,weight in graph(current) :
            new_cost = cost + weight
            pq.append(new_cost,neighbour,path +[neighbour])

    return None


for neighbour ,weight in graph(current) :
    new_cost = cost + weight 
    pq.append(new_cost,neighbour,path)


import heapq
def ucs(graph,start,goal) :
    pq = [(0,start,[start])]

    visited = set()

    while pq :
        current,path,cost = heapq.heappop(pq) 
        if current == goal :
            return path
        if current not in visited :
            visited.add(current)

            for neighbour,weight in graph(current):
                new_cost = cost + weight
                pq.append(new_cost,neighbour,path+[neighbour])
        return None
