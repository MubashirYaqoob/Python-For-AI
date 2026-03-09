import heapq
def ucs(graph,start,goal) :
    pq = [(0,start,[start])]
    visited = set() 

    while pq :
        cost,current,path = heapq.heappop()

        if current == goal :
            return path 
        if current not in visited :
            visited.add(current) 

            for neighbour ,weight in graph(current) :
                new_cost = cost + weight 
                pq.append(new_cost,neighbour,path+[neighbour])
            