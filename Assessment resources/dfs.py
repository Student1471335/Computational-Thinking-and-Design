def dfs(graph, start, target, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == target:
        print(f"Path: {' -> '.join(path)}")
        return path

    for neighbour in graph[start]:
        if neighbour not in path:
            new_path = dfs(graph, neighbour, target, path)
            if new_path:
                return new_path

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

solution = dfs(graph, "A", "H")
print(solution)
