def walk(graph, curr, needle, seen, path):
    if seen[curr]:
        return False
    seen[curr] = True
    path.append(curr)
    if curr == needle:
        return True
    list = graph[curr]
    for i in range(len(list)):
        edge = list[i]
        if walk(graph, edge.to, needle, seen, path):
            return True
    path.pop()
    return False

def dfs(graph, source, needle):
    seen = [] * len(graph)
    path = []
    walk(graph, source, needle, seen, path)

    if len(path) == 0:
        return None
    return path