def depthFirstPrint1 (graph, source):
  stack = [source]
  while len(stack) > 0:
    current = stack.pop()
    print(current)
    for neighbor in graph[current]:
      stack.append(neighbor)

def depthFirstPrint (graph, source):
  print(source)
  for neighbor in graph[source]:
    depthFirstPrint(graph, neighbor)


graph = {
  "a": ['b', 'c'],
  "b": ['d'],
  "c": ['e'],
  "d": ['f'],
  "e": [],
  "f": []
}

depthFirstPrint(graph, 'a')