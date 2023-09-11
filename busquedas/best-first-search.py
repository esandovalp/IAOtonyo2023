import heapq

def best_first_search(graph, start, goal, heuristic):
    open_list = [(heuristic(start, goal), start)]
    closed_set = set()
    came_from = {}

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(came_from, goal)

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_set:
                cost = heuristic(neighbor, goal)
                heapq.heappush(open_list, (cost, neighbor))
                came_from[neighbor] = current_node
    
    return None

def reconstruct_path(came_from, node):
    path = [node]
    while node in came_from:
        node = came_from[node]
        path.append(node)
    return list(reversed(path))

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

start_node = 'A'
goal_node = 'H'

heuristic = lambda node, goal: abs(ord(node) - ord(goal))  # A simple heuristic function (difference in ASCII values)

path = best_first_search(graph, start_node, goal_node, heuristic)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
