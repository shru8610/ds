from collections import deque

# -----------------------------
# DFS using Adjacency Matrix
# -----------------------------
def dfs(matrix, start, visited, nodes):
    print(nodes[start], end=" ")
    visited[start] = True
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, i, visited, nodes)


# -----------------------------
# BFS using Adjacency List
# -----------------------------
def bfs(adj_list, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    # Define graph nodes (locations)
    nodes = ['A', 'B', 'C', 'D', 'E']
    n = len(nodes)

    # Adjacency Matrix for DFS (routes)
    #     A  B  C  D  E
    matrix = [
        [0, 1, 1, 0, 0],  # A connected to B, C
        [1, 0, 0, 1, 0],  # B connected to A, D
        [1, 0, 0, 1, 1],  # C connected to A, D, E
        [0, 1, 1, 0, 1],  # D connected to B, C, E
        [0, 0, 1, 1, 0]   # E connected to C, D
    ]

    # Adjacency List for BFS (same graph)
    adj_list = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }

    # Starting node
    start_node = 'A'
    start_index = nodes.index(start_node)

    print("=== Depth First Search (DFS) using Adjacency Matrix ===")
    visited = [False] * n
    dfs(matrix, start_index, visited, nodes)

    print("\n\n=== Breadth First Search (BFS) using Adjacency List ===")
    bfs(adj_list, start_node)
