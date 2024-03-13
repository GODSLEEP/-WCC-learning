import heapq

def prim(graph):
    mst = []
    mst_set = set()
    priority_queue = [(0, list(graph.keys())[0])]  # Start from an arbitrary vertex

    while priority_queue:
        weight, vertex = heapq.heappop(priority_queue)

        if vertex not in mst_set:
            mst_set.add(vertex)
            mst.append((weight, vertex))

            for neighbor, neighbor_weight in graph[vertex].items():
                if neighbor not in mst_set:
                    heapq.heappush(priority_queue, (neighbor_weight, neighbor))

    return mst

# Example graph represented as adjacency list
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 1, 'C': 2}
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
