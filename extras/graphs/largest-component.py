def largestComponent(graph):
  visited = set()
  largest = 0
  for node in graph:
    count = exploreSize(graph, node, visited)
    largest = max(count, largest)
  return largest

def exploreSize(graph, current, visited):
  if current in visited: return 0
  visited.add(current)
  count = 1
  for neighbor in graph[current]:
    count += exploreSize(graph, neighbor, visited)
  return count

def largestComponentBFS(graph):
  visited = set()
  largest = 0
  for node in graph:
    queue = [node]
    if node in visited:
        continue
    count = 0
    while len(queue) > 0:
      current = queue.pop(0)
      if current in visited:
        continue
      visited.add(current)
      count+=1
      for neighbor in graph[current]:
        queue.append(neighbor)
    largest = max(largest, count)
  return largest





graph = {
  "1": ['2'],
  '2': ['1','8'],
  '6': ['7'],
  '9': ['8'],
  '7': ['6', '8'],
  '8': ['9', '7', '2']
}

print(largestComponentBFS(graph))


