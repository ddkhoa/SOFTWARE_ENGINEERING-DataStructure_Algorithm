"""
    Breath First Search: algorithm to traverse a graph or a tree
    visit all the adjacent nodes before going further
"""


def bfs(visited: set, queue: list, graph, node):

    queue.append(node)

    while len(queue) > 0:
        node = queue.pop(0)

        if node not in visited:

            print(node, end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                queue.append(neighbour)


#         5
#       /   \
#     3       7
#    /  \       \
# 2       4   -    8
graph = {
    '5': ['3', '7'],
    '3': ['2', '4', '7'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

bfs(set(), [], graph, '5')  # 5 3 7 2 4 8
