

def dfs (graph,start,goal) :

    stack = [(start,[start])] # -- here we used list 
    visited = set() 

    while stack :
        current,path = stack.pop()

        if current == goal :
            return path
        if current not in visited :
            visited.add(current)

            for neighbour in graph(stack) :
                stack.append((neighbour,path+[neighbour]))
    return None


def dfs(graph,goal,start) :
    stack  = [(start,[start])] # -- stack bana diya he me ne 
    visited = set()

    while stack:
        current,path = stack.pop()

        if current == goal :
            return path
        if current not in visited:
            visited.add(current)

            for neighbour in graph(stack):
                stack.append(neighbour,path+neighbour)
    return None
