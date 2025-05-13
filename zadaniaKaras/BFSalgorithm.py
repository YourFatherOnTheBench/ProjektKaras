
tree = {
    'A': ['C', 'B'],
    'C': ['D', 'E'],
    'B': ['F'],
    'D': [],
    'E': [],
    'F': []
}
visited = []
def BFS(tree, start):

    queue = [start]
    visited.append(start)
    while queue:
        node = queue.pop(0)
        for child in tree[node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)


BFS(tree, 'A')
print(visited)