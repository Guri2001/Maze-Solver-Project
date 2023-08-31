"""Calcultest the Manhattan distance by taking the difference between two points 
    across the x axis and y a axis to find distance. It's used as an heuristic cost function 
    for the A* algorithm"""
def manhattan_distance(pos1, pos2):
    x1,y1 = pos1
    x2,y2 = pos2

    return abs(x2-x1) + abs(y2-y1)

"""Claculates the shortest path/solution to the maze provided a starting point optional args 
    and the maze which it needs to find the solution for."""
def aStar(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    
    open_set = {start} #The cells which haven't been visited. 
    
    came_from = {} #Stores path of every cell which we come from previously.
    
    # Initialize g_score and f_score dictionaries for each cell in the maze
    g_score = dict.fromkeys(m.grid, float("inf"))  
    f_score = dict.fromkeys(m.grid, float("inf"))

    # Set the g_score for the starting cell to 0
    g_score[start] = 0

    # Set the f_score for the starting cell to its estimated cost to reach the goal
    f_score[start] = manhattan_distance(start, m._goal)

    # stores the search path
    search_path = [start]
    
    #Loop until the open set is empty.
    while open_set:
        currCell = min(open_set, key=lambda x: f_score[x])
        open_set.remove(currCell)
        search_path.append(currCell)
        if currCell == m._goal:
            break        
        #Check every neighbour at current cell 
        for direction in 'ESNW':
            if m.maze_map[currCell][direction]:
                if direction == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif direction == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif direction == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif direction == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                #Calculate gtenatitive g_score for child cell
                temp_g_score = g_score[currCell] + 1

                #If the tentative g_score is less than g_score for child cell update the scores and add child cell to open set 
                if temp_g_score < g_score.get(childCell, float('inf')):   
                    came_from[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + manhattan_distance(childCell, m._goal)
                    if childCell not in open_set:
                        open_set.add(childCell)
                        
    #Create a path to store final path which takes you to the goal storing shortest path.
    path = {}
    cell = m._goal
    while cell != start:
        path[came_from[cell]] = cell
        cell = came_from[cell]
    return search_path,came_from,path


