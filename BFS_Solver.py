from collections import deque

def BFS(maze, start=None):

    if start is None:
        start = (maze.rows, maze.cols)
    queue = deque([start]) #Queue to store the next place it needs to visit in the maze.
    already_visited_coords = set([start]) # Already visited places in the maze
    parent_coords = {start: None} # To store parent node of each cell in the maze it visits. It allows
                                  # to construct the shortest path from start to end. 
    
    all_visited_coords = [] # Stores all visited points during the BFS. Useful for visualising every point.

    while queue:  #Until the queue is not empty we run the loop or until the goal point is reached.
        curr = queue.popleft() #Remove the point from front of queue and store its value in curr.
        
        #If the value we check is our goal value we store
        if curr == maze._goal:  
            break
        """
        Otherwise we run a loop to check where next we can visit N E W S. We visit the node 
        which hasn't been visited before we add to the already_visited the rows and cols along 
        in the queue. We make the parent_coords the next point we are at where again from we can 
        visit N E W S and we add that to all_visited_coords so far. 

        """ 
        
        for d_row, d_col, directions in [(0, 1, "E"), (0, -1, "W"), (1, 0, "S"), (-1, 0, "N")]:
            row, col = curr[0] + d_row, curr[1] + d_col #Update rows and cols each time to correct points based on direction.


            if (row, col) in already_visited_coords or not maze.maze_map[curr][directions]:
                continue

            already_visited_coords.add((row, col))
            queue.append((row, col))
            parent_coords[(row, col)] = curr
            all_visited_coords.append((row, col))

    # We compute the shortest path from starting point (1,1) to the goal which is the bottom right point always.

    shortest_path = {} #Stores shortest path
    cell = maze._goal  
    # We start from the goal node and find our way back to the start node. 
    while cell != start:
        #Add to shortest path 
        shortest_path[parent_coords[cell]] = cell
        # Make current cell as the new parent_coords
        cell = parent_coords[cell] # Update cell to new parent location.

    #We the shortest path, all visited values. 
    return all_visited_coords, parent_coords, shortest_path

