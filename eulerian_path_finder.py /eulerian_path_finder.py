from collections import defaultdict

def find_eulerian_path(graph):
    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop(0)
            dfs(next_node)
        path.append(node)

    in_degrees = defaultdict(int)
    out_degrees = defaultdict(int)

    for node, neighbors in graph.items():
        out_degrees[node] += len(neighbors)
        for neighbor in neighbors:
            in_degrees[neighbor] += 1

    start_node = None
    end_node = None

    for node in graph.keys():
        if in_degrees[node] < out_degrees[node]:
            start_node = node
        elif in_degrees[node] > out_degrees[node]:
            end_node = node

    # Connect the unbalanced nodes
    if start_node is not None and end_node is not None:
        graph[end_node].append(start_node)
    else:
        for node in graph.keys():
            if out_degrees[node] > 0:
                start_node = node
                break

    path = []
    if start_node is not None:
        dfs(start_node)
        path = path[::-1]

    return path

# Sample Input with new data and all nodes present
adjacency_list = {
    2: [3],
    1: [0, 9],
    2: [1],
    3: [2, 6],
    4: [],
    5: [3],
    6: [],
    7: [1],
    8: [7],
    9: [8]
}

# Find and print the Eulerian path
eulerian_path = find_eulerian_path(adjacency_list)
print(" ".join(map(str, eulerian_path)))
