import random

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
        line = []
        for j in range(0, width):
            line.append(' ')
        grid.append(line)

# Adding obstacles
grid[7][9] = 'X'
grid[7][8] = 'X'
grid[7][6] = 'X'
grid[8][6] = 'X'

"""
Add an additional 20 randomly placed obstacles and print their location
using the format [(x1,y1), (x2,y2),...]
"""

# Set number of additional randomly placed obstacles
obstacles = 20

# Initialising list where the location of obstacles will be stored
obstacleLocation = []

for i in range(0, obstacles):
    placed = False
    while placed == False:
        # Pick a random coordinate
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        # Check that there are no obtacles in that coordinate already
        if grid[y][x] == ' ':
            grid[y][x] = 'X'
            obstacleLocation.append((x,y))
            placed = True

# Print obstacle locations on screen
print("Obstacle coordinates: ", obstacleLocation)

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
path = []

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
    at = (deliveryX, deliveryY)
    while at != None:
        path.append(at)
        at = previous[at[1]][at[0]]
    path.reverse()

    # Print number of steps in the CLI
    print("Number of steps: ", len(path))
    # Print path in the CLI
    print("Path: ", path)

    """
    In the event that your vehicle is unable to reach its destinantion,
    your algorithm should print "Unable to reach delivery point" and identify
    which obstacles need to be removed in order for the vehicle to reach its
    destination.

    Your algorith should suggest the least amount of obstacles using the format
    [(x1,y1),(x2,y2)...] in order for your vehicle to reach its destination.
    """

else:
    print("Unable to reach delivery point")

for i in path:
    grid[i[1]][i[0]] = "#"

# Print grid in the CLI
for row in grid:
    print(row)