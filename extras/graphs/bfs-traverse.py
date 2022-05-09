def breadthFirstPrint(graph, source):
  queue = [source]
  while len(queue):
    current = queue.pop(0)
    print(current)
    for neighbor in graph[current]:
      queue.append(neighbor)



graph = {
  "a": ['b', 'c'],
  "b": ['d'],
  "c": ['e'],
  "d": ['f'],
  "e": [],
  "f": []
}

breadthFirstPrint(graph, 'a')