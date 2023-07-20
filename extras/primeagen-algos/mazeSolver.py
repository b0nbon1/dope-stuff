direction = [
    [-1, 0],
    [1, 0],
    [0,-1],
    [0,1],
]

def walk(maze, wall, curr, end, seen, path):
    # off the maze
    if curr["x"] < 0 or curr["x"] > len(maze[0])-1 or curr["y"] < 0 or curr["y"] > len(maze)-1 or maze[curr["y"]][curr["x"]] == wall or seen[curr["y"]][curr["x"]]:
        return False


    if curr["x"] == end["x"] and curr["y"] == end["y"]:
        path.append(end)
        return True
    
    seen[curr["y"]][curr["x"]] = True
    path.append(curr)

    for i in range(len(direction)):
        x, y = direction[i][0], direction[i][1]
        if walk(maze, wall, {
            "x": curr["x"] + x,
            "y": curr["y"] + y
        }, end, seen, path):
            return True

    path.pop()

    return False
    

def maze_solver(maze, wall, start, end):
    seen = []
    path = []

    for i in range(len(maze)):
        seen.append([False]*len(maze[0]))

    walk(maze, wall, start, end, seen, path)

    return path


maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]

mazeResult = [
        { "x": 10, "y": 0 },
        { "x": 10, "y": 1 },
        { "x": 10, "y": 2 },
        { "x": 10, "y": 3 },
        { "x": 10, "y": 4 },
        { "x": 9, "y": 4 },
        { "x": 8, "y": 4 },
        { "x": 7, "y": 4 },
        { "x": 6, "y": 4 },
        { "x": 5, "y": 4 },
        { "x": 4, "y": 4 },
        { "x": 3, "y": 4 },
        { "x": 2, "y": 4 },
        { "x": 1, "y": 4 },
        { "x": 1, "y": 5 },
    ]

start = { "x": 10, "y": 0 }
end = { "x": 1, "y": 5 }

result = maze_solver(maze, "x", start, end)

print(result == mazeResult)