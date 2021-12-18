# Creating graph
Graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'G': ['E', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A'],
}

# function to perform DSF
def DFS(Graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in Graph[node]:
            DFS(Graph, n, visited)
    return visited


start = input("Enter the first vertex (A, B, C, D, E, F, G, H): ")
print("The Depth First Search of the following Graph is: ")
visited = DFS(Graph, start, [])
for i in visited:
    print(i, end='   ')
