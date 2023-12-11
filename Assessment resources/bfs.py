from collections import deque


def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current_node, path = queue.popleft()

        if current_node == target:
            print(f"Path from {start} to {target}: {' -> '.join(path)}")
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C"],
    "H": ["E"],
}

# Starting DFS from node 'A'
solution = bfs(graph, "A", "H")
print(solution)
