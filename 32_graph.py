def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(graph[node] - visited)
        
graph = {'A': {'B', 'C'}, 'B': {'A','D'}, 'C': {'A', 'D'}, 'D': {'B', 'C'}}
dfs(graph, 'A')
print(graph)