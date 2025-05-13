

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = {
    'A': 0,
    'B': float('inf'),
    'C': float('inf'),
    'D': float('inf')
}
explored = []
prev = {
    'A': None,
    'B': None,
    'C': None,
    'D': None
}
sum = 0
def shortest_path(current, dest):
    
    
    while dest not in explored:
        explored.append(current)
        if dest in explored:
            break
        update_estimates(current)
        node = choose_next_node(current)

        current = node
 
            

def update_estimates(node):
    for child, value in graph[node].items():
        if child not in explored:
            if distances[node] + value < distances[child]:
                distances[child] = distances[node] + value
                prev[child] = node
        
def choose_next_node(node):
    minimum = float('inf')
    nodes_list = [child for child in graph[node] if child not in explored]

    for child in nodes_list:
        if distances[child] < minimum:
            minimum = distances[child]
            next_node = child
    return next_node

shortest_path( 'A', 'D')     
print(distances)
print(explored)
print(prev)
print(sum)