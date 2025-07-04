import heapq

def best_first_search(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()
    parent = {start: None}

    while priority_queue:
        current_heuristic, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                parent[neighbor] = current_node

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}
heuristic = {
    'A' : 6,
    'B' : 4,
    'C' : 4,
    'D' : 0,
    'E' : 2,
    'F' : 3,
    'G' : 1
}

start = 'A'
goal = 'D'

path = best_first_search(graph, start, goal, heuristic)
print("Best First Search Path: ", path)

#OUTPUT:
"""
Best First Search Path:  ['A', 'B', 'D']
"""