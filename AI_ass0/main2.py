# Creating graph
graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '5'],
    '4': ['2', '5', '6'],
    '5': ['2', '3', '4', '6'],
    '6': ['4', '5']
}

visited = []  # list for visited nodes
queue = []  # to initialise queue

# function to perform BSF
def BFS(visited, graph, current_node):
    visited.append(current_node)
    queue.append(current_node)
    while queue:                  # Creating loop to visit each node
        s = queue.pop(0)
        print(s, end="   ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start = input("Enter the starting vertex (1, 2, 3, 4, 5, 6) :  ")
print("The Breadth First Search of the following Graph is: ")
BFS(visited, graph, start)
