**BFS Example: Shortest Path in an Unweighted Graph**

BFS is an ideal application for finding the shortest path in an unweighted graph. This explores all the neighbors of a node before moving on to the next level, ensuring that the shortest path to each node is discovered first.

**Efficiency for BFS in Shortest Path:**

- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
- Space Complexity: O(V), where V is the number of vertices.





**DFS Example: Connected Components in an Undirected Graph**

DFS is an ideal application for finding connected components in an undirected graph. It explores as far as possible along each branch before backtracking, which naturally helps identify connected components.

**Efficiency for DFS in Connected Components:**

- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
- Space Complexity: O(V), where V is the number of vertices.

**How DFS Connected Components Algorithm Works:**

- The algorithm starts from an unvisited node and explores as far as possible along each branch before backtracking.
- It marks visited nodes to avoid revisiting them.
- For each unvisited node, it initiates a DFS traversal and forms a connected component by adding all reachable nodes.
- The process repeats until all nodes are visited, and all connected components are identified.