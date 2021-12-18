# defining variables
nodes = {
    0: 'V',
    1: 'I',
    2: 'B',
    3: 'G',
    4: 'Y',
    5: 'O',
    6: 'R',
}

# graph connctions
graph = {
    0: [1, 4],
    1: [2, 5, 4],
    2: [0, 1, 3],
    3: [1, 6, 3],
    4: [0, 1, 3],
    5: [2, 4, 6],
    6: [0, 1, 3],

}

n = 0
i = 0
graph_colour = {}

colors = ["Red", "Green", "Blue"]  # colour of nodes


def check(node, colour):
    for i in graph[node]:
        if i in graph_colour and graph_colour[i] == colour:
            return False
    return True


def assign(node, colour):
    graph_colour[node] = colour


while n < 7:
    assigned = 0
    for i in range(3):
        if check(n, i) == True:
            assign(n, i)
            n += 1
            assigned = 1
            break

    if assigned == 0:
        prevas = 0
        for x in range(3):
            if check(n-1, (graph_colour[n-1]+1) % 3) == True:
                assign(n, (graph_colour[n-1]+1) % 3)
                prevas = 1
                break
        if prevas == 0:
            n -= 1

for key, value in graph_colour.items():
    print(nodes[key] + " : " + colors[value])
