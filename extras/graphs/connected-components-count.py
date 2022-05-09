def connectedComponentCountDFS(graph):
  visited = set()
  count = 0
  for node in graph:
    if exploreDFS(graph, node, visited):
      count += 1
  return count

def exploreDFS(graph, current, visited):
  if current in visited: return False
  visited.add(current)
  for neighbor in graph[current]:
    exploreDFS(graph, neighbor, visited)

  return True

def connectedComponentCountBFS(graph):
  visited = set()
  count = 0
  for node in graph:
    queue = [node]
    if node in visited:
        continue
    while len(queue) > 0:
      current = queue.pop(0)
      if current in visited:
        continue
      visited.add(current)
      for neighbor in graph[current]:
        queue.append(neighbor)
    count+=1
  return count


  
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

print(connectedComponentCountBFS(graph))