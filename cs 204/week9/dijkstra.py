import heapq

def dijkstra(graph, source):
    dist = {vertex: float('inf') for vertex in graph}
    dist[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > dist[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist

# Example graph represented as adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from source node", source_node, ":", shortest_distances)
