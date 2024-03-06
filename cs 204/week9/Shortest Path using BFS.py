from collections import deque

def shortest_path_bfs(graph, start, end):
    if start not in graph or end not in graph:
        return None  # Invalid input
    
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path  # Found the shortest path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No path found

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_node = 'A'
end_node = 'G'
shortest_path = shortest_path_bfs(graph, start_node, end_node)

print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
