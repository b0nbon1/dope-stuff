'''
edges = [         graph = {
  [i,j],                    i: [j,k],
  [k,i],    ==>             j: [i],
  [m,k],                    k: [i,m,l],
  [k,l],                    m: [k],
  [o,n]                     l: [k],
]                           o: [n],
                            n: [o]
                          }
'''

def undirectPath(edges, nodeA, nodeB):
  graph = buildGraph(edges)
  return hasPathDFS(graph, nodeA, nodeB, set())

def hasPathDFS(graph, src, dst, visited):
  if src == dst: return True
  if src in visited: return False
  visited.add(src)
  for neighbor in graph[src]:
   if  hasPathDFS(graph, neighbor, dst, visited) == True:
     return True
  return False

def hasPathBFS(graph, src, dst):
  visited = set()
  queue = [src]
  while len(queue) > 0:
    current = queue.pop(0)
    if current == dst: return True
    if current in visited: continue
    visited.add(current)
    for neighbor in graph[current]:
      queue.append(neighbor)
  return False

def undirectPathBFS(edges, nodeA, nodeB):
  graph = buildGraph(edges)
  return hasPathBFS(graph, nodeA, nodeB)



def buildGraph(edges):
  graph = {}
  for edge in edges:
    a, b = edge[0], edge[1]
    if not (a in graph): graph[a] = []
    if not (b in graph): graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

# edges = [
#   ["i","j"], 
#   ["k","i"],
#   ["m","k"],
#   ["k","l"], 
#   ["o","n"]
# ]

edges = [[2,1,1],[2,3,1],[3,4,1]]
print(buildGraph(edges))
# print(undirectPathBFS(edges, "j", "i"))