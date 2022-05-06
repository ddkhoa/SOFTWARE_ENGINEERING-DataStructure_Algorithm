"""
    Deep First Search: algorithm to traverse a graph or a tree
    go as far as possible before going back
"""


def dfs(visited, graph, node):
    if node not in visited:

        # visit the node
        print(node, end=" ")

        # add to visited to avoid revisit
        visited.add(node)

        # visit neighbour nodes
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


#         5
#       /   \
#     3       7
#    /  \       \
# 2       4   -    8
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
dfs(set(), graph, '5')  # 5 3 2 4 8 7
