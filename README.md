### Eulerian Path Finder Using Hierholzer’s Algorithm (with Correction for Unbalanced Graphs)
This script implements an algorithm to find an Eulerian path in a directed graph represented as an adjacency list. It uses a modified version of Hierholzer’s algorithm and handles graphs with exactly two unbalanced nodes (a necessary condition for an Eulerian path).

### What It Does
* Builds the in-degree and out-degree for each node.
* Identifies the start and end node based on degree imbalance.
* If imbalance is found, it temporarily connects the end node to the start node.
* Performs a depth-first search (DFS) to construct the path.
* Reverses the path to get the correct order.

###  Code Explained
### 1. Depth-First Search (DFS)

```
   def dfs(node):
    while graph[node]:
        next_node = graph[node].pop(0)
        dfs(next_node)
    path.append(node)
```
This recursive DFS walks edges until it gets stuck, then backtracks — this is core to Hierholzer’s algorithm.


### 2. Calculate In-Degrees and Out-Degrees

```
in_degrees = defaultdict(int)
out_degrees = defaultdict(int)

for node, neighbors in graph.items():
    out_degrees[node] += len(neighbors)
    for neighbor in neighbors:
        in_degrees[neighbor] += 1
```
This identifies if the graph is balanced (Eulerian circuit) or unbalanced (Eulerian path).

### 3. Identify Start and End Nodes
```
for node in graph.keys():
    if in_degrees[node] < out_degrees[node]:
        start_node = node
    elif in_degrees[node] > out_degrees[node]:
        end_node = node
```
If one node has out-degree > in-degree, it becomes the starting node for the path.

### 4. Fix for Unbalanced Graphs

``` if start_node is not None and end_node is not None:
    graph[end_node].append(start_node)```

```
A temporary edge is added to make the graph Eulerian (a circuit), allowing DFS traversal.

### 5. Run the DFS and Reconstruct Path
```
path = []
dfs(start_node)
path = path[::-1]
```
After DFS, the path is reversed to yield the correct Eulerian path order.

### Example
Input:
```adjacency_list = {
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
```

Output:
5 3 6 3 2 1 9 8 7 1 0


### How to Use
Paste your graph as a Python dictionary (adjacency_list).

Call find_eulerian_path(adjacency_list).
The function will return a list with the ordered path.

### Requirements
Python 3.x
No external libraries (uses only collections)

### License
MIT License










 








