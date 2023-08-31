from collections import deque

def rotate_clockwise():
    global direction
    keys, values = deque(direction.keys()), deque(direction.values())
    values.rotate(1)
    direction = dict(zip(keys, values))

def rotate_counterclockwise():
    global direction
    keys, values = deque(direction.keys()), deque(direction.values())
    values.rotate(-1)
    direction = dict(zip(keys, values))

def move_forward(cell):
    x, y = cell
    forward_direction = direction['forward']
    dx, dy = {
        'E': (0, 1),
        'W': (0, -1),
        'N': (-1, 0),
        'S': (1, 0)
    }[forward_direction]
    return (x+dx, y+dy), forward_direction
def wall_follower(maze):
    global direction
    #Directions that can be travelled in.
    direction = {'forward': 'N', 'left': 'W', 'back': 'S', 'right': 'E'}
    #The current cell in the maze which is the starting cell default to (1,1)
    curr_cell = (maze.rows, maze.cols)
    #Stores the path of the solution.
    path = ''
    
    # Loops until a goal cell is found otherwise its stuck in an infinite loop.
    # Only works on perfect mazes.
    while True:
        #If goal cell found stop
        if curr_cell == (1, 1):
            break
        # If the current cell has a left wall 
        if maze.maze_map[curr_cell][direction['left']] == 0:
            #If the current cell has a forward wall
            if maze.maze_map[curr_cell][direction['forward']] == 0:
                rotate_clockwise() #We rotate clockwise
            else:
                #Otherwise simply move forward
                curr_cell, d = move_forward(curr_cell)
                path += d #Add to the path the direction of travel e.g. N,E,W, or S
        else:
            #If there is no wall on left then we move clockwise 
            rotate_counterclockwise()
            #And move forward
            curr_cell, d = move_forward(curr_cell)
            path += d #Add the direction of movement to the path
    
    #Get the path without any repitions it returns the shortest path to get to the goal node if it can.
    path2 = ''.join([d for i, d in enumerate(path) if i==0 or d!=path[i-1]])
    
    #Two paths are returned first one contains all possible paths travelled and second is the 
    # shortest path taken to get to that point avoiding any repitions in the process. 
    return path, path2

