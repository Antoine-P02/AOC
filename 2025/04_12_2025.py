

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    count = 0
    grid = []

    for l in lines:
        data = list(l.strip())
        grid.append(data)
    
    print(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (grid[x][y] == "@"):
                if ( checkAround(grid, x, y, len(grid), len(grid[0]) ) < 4 ):
                    count += 1
                    grid[x][y] = "x"

    display(grid, count)

def display(grid, count):
    print("-"*50)
    for x in grid:
        print(x)
    print("-"*50, "count :", count)

def checkAround(grid, x, y, maxX, maxY):

    pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    paperCount = 0

    for p in pos:
        px = x + p[0]
        py = y + p[1]
        if ( 0 <= px < maxX and 0 <= py < maxY):
            paperCount += grid[px][py] == "@"
            paperCount += grid[px][py] == "x"

    return paperCount



print(naive("2025/input4"))
print("--------------------------------")



def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    count = 0
    grid = []

    for l in lines:
        data = list(l.strip())
        grid.append(data)
    
    print(grid)
    for _ in range(50):
        for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if (grid[x][y] == "@"):
                        if ( checkAround(grid, x, y, len(grid), len(grid[0]) ) < 4 ):
                            count += 1
                            grid[x][y] = "."

    display(grid, count)


def checkAround2(grid, x, y, maxX, maxY):

    pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    paperCount = 0

    for p in pos:
        px = x + p[0]
        py = y + p[1]
        if ( 0 <= px < maxX and 0 <= py < maxY):
            paperCount += grid[px][py] == "@"

    return paperCount


print(naive2("2025/input4"))
print("Disgusting bruteforce 50 times to reapply algorithm to the changing grid")
print("--------------------------------")
