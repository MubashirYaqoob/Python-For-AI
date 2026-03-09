from collections import deque

def bfs(graph,start,goal) :

    queue = deque([(start,[start])]) # -- mein A pr hun or abtk ka rasta [A ] hai 

    visited = set() # -- y vist kar chuka hun 

    node,path = queue.popleft() # -- current room and total path 

    if node == goal :
        return path
    
    if node not in visited :
        visited.add(node)
    
    for neighbour in graph([node]):
        queue.append([neighbour,path +[neighbour]])




from collections import deque 

def bfs(graph,start,goal) :

    queue = deque([(start,[start])])
    visited = set() 
    while queue :
        current,path = queue.popleft()

        if current == goal :
            return path
        if current not in visited :
            visited.add(current)

            for neighbour in graph[current] :
                if neighbour not in visited :
                    queue.append(neighbour,path+[neighbour])
    return None

    