def hasUnvisited(seen, dists):
    for i in range(len(seen)):
        if not seen[i] and dists[i] < float("inf"):
            return True
    return False

def getLowestUnvisited(seen, dists):
    idx = -1
    lowestDistance = float("inf")
    for i in range(len(seen)):
        if seen[i]:
            continue
        if lowestDistance > dists[i]:
            lowestDistance = dists[i]
            idx = i
    return idx

def dijkstra(source, sink, arr):
    seen = [False] * len(arr)
    prev = [-1] * len(arr)
    dists = [float('inf')] * len(arr)
    dists[source] = 0

    while hasUnvisited(seen, dists):
        curr = getLowestUnvisited(seen, dists)
        seen[curr] = True

        adjs = arr[curr]
        for i in range(len(adjs)):
            edge = adjs[i]
            if seen[edge["to"]]:
                continue
            
            dist = dists[curr] + edge["weight"]
            if dist < dists[edge["to"]]:
                dists[edge["to"]] = dist
                prev[edge["to"]] = curr
    result = []
    curr = sink
    while prev[curr] != -1:
        result.append(curr)
        curr = prev[curr]
    result.append(source)
    result.reverse()
    return result

list1 = [None] * 7
list1[0] = [
    { "to": 1, "weight": 3 },
    { "to": 2, "weight": 1 },
]
list1[1] = [
    { "to": 0, "weight": 3 },
    { "to": 2, "weight": 4 },
    { "to": 4, "weight": 1 },
]
list1[2] = [
    { "to": 1, "weight": 4 },
    { "to": 3, "weight": 7 },
    { "to": 0, "weight": 1 },
]
list1[3] = [
    { "to": 2, "weight": 7 },
    { "to": 4, "weight": 5 },
    { "to": 6, "weight": 1 },
]
list1[4] = [
    { "to": 1, "weight": 1 },
    { "to": 3, "weight": 5 },
    { "to": 5, "weight": 2 },
]
list1[5] = [
    { "to": 6, "weight": 1 },
    { "to": 4, "weight": 2 },
    { "to": 2, "weight": 18 },
]
list1[6] = [
    { "to": 3, "weight": 1 },
    { "to": 5, "weight": 1 },
]
    
print(dijkstra(0, 6, list1))


