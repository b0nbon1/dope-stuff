def shortestPath(edges, nodeA, nodeB):
  graph = buildGraph(edges)
  queue = [nodeA]
  while len(queue) > 0:
    curr = queue.pop(0)
    if curr == nodeB: return True
    for neighbor in graph[curr]:
      queue.append(neighbor)

def buildGraph(edges):
  graph = {}
  for edge in edges:
    a, b = edge[0], edge[1]
    if not (a in graph): graph[a] = []
    if not (b in graph): graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v'],
]
shortestPath(edges, 'w', 'z')
