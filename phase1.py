"""
Implement a 10x10 grid that contains a starting point on (0,0),
the delivery point on (9,9) and the following obstacles on
locations (9,7) (8,7) (6,8)
"""

# Set width and size
height = 10
width = 10

# Generate grid with no obstacles
grid = []
for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(' ')
        grid.append(row)

# Adding obstacles
grid[7][9] = 'X'
grid[7][8] = 'X'
grid[7][6] = 'X'
grid[8][6] = 'X'

# Setting starting point
startX = 0
startY = 0
grid[startY][startX] = '0'

# Setting delivery point
deliveryX = 9
deliveryY = 9
grid[deliveryY][deliveryY] = '*'

"""
Your algorithm should calculate a valid path avoiding the obstacles and
reaching the delivery point.

Your solution should print the path in the format of
[(x1,y1),(x2,y2)...] and also the number of steps.
"""

# Counters to keep track of layers in the Breadth First Search Algorithm
nodesInNextLayer = 0
nodesLeftInLayer = 1

# Direction vectors (Vertical, horizontal and diagonal)
directionX = [-1, 1, 0, 0, 1, -1, -1, 1]
directionY = [0, 0, -1, 1, 1, -1, -1, 1]

# Generate matrix to check whether a cell has been visited or not
visited = []
for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(False)
        visited.append(row)

# Generate matrix that stores the previous cell so we can
# reconstruct the path once one its found
previous = []
for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(None)
        previous.append(row)

#Queues that stores the x and y coordinates of the cells
# we will visit next
qX = []
qY = []

# Visit starting point
qX.append(startX)
qY.append(startY)
visited[startY][startX] = True

delivered = False

while len(qX) > 0:
    currentX = qX.pop(0)
    currentY = qY.pop(0)
    if grid[currentY][currentX] == '*':
        delivered = True
        break
    # Explore neighbouring cells
    for i in directionX:
        x = currentX + directionX[i]
        y = currentY + directionY[i]
        # Skip out of bounds
        if x < 0 or y < 0:
            continue
        if x >= width or y >= height:
            continue
        # Skip visited locations
        if visited[y][x] == True:
            continue
        # Skip obstacles
        if grid[y][x] == 'X':
            continue
        qX.append(x)
        qY.append(y)
        previous[y][x] = (currentX, currentY)
        visited[y][x] = True
        nodesInNextLayer += 1

    nodesLeftInLayer -= 1
    if nodesLeftInLayer == 0:
        nodesLeftInLayer = nodesInNextLayer
        nodesInNextLayer = 0

if delivered == True:
    # Reconstruct the path
    path = []
    at = (deliveryX, deliveryY)
    while at != None:
        path.append(at)
        at = previous[at[1]][at[0]]
    path.reverse()

    # Print number of steps in the CLI
    print("Number of steps: ", len(path))
    # Print path in the CLI
    print("Path: ", path)
else:
    print("Path not found")

# Print grid in the CLI
for row in grid:
    print(row)