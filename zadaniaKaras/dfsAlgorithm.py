

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def DFS(tree, current):

     
    visited.append(current)
    for child in tree[current]:
        if child not in visited:
            DFS(tree, child)
        
    


DFS(tree, 'A')
print(visited)