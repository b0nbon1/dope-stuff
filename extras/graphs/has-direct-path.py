# direct graph
def hasPath(graph, src, dst):
  if src == dst: return True
  for neighbor in graph[src]:
    if hasPath(graph, neighbor, dst) == True:
      return True
  return False

graph = {
  "f": ["g", "i"],
  "g": ["h"],
  "h": [],
  "i": ["g", "k"],
  "j": ["i"],
  "k": []
}

print(hasPath(graph, "f", "k"))

def bfsHasPath(graph, src, dst):
  queue = [src]
  while len(queue) > 0:
    curr = queue.pop(0)
    if curr == dst: return True
    for neighbor in graph[curr]:
      queue.append(neighbor)
  return False

print(bfsHasPath(graph, "f", "k"))
