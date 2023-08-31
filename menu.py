import tkinter as tk
from tkinter import ttk
from pymaze import maze, textLabel, agent, COLOR
import time
import Astar_solver
from tkinter import filedialog
import BFS_Solver
import wallFollower_solver


# Create main menu window
root = tk.Tk()

# Set window title and size
root.title("Main Menu")
root.geometry("400x450")

# Create a gradient background
background_color = '#%02x%02x%02x' % (35, 45, 70)
bg_gradient = ttk.Style()
bg_gradient.configure("bg.TFrame", background=background_color)
frame = ttk.Frame(root, style="bg.TFrame")
frame.place(relwidth=1, relheight=1)

# Create a label widget and set its text to the window title
title_label = tk.Label(root, text="Maze Solver", font=("Helvetica", 30), foreground="#FFFFFF", background=background_color, padx=20, pady=20)
title_label.pack()

# Create a separator line
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=20)

# Create a label widget with a subtitle
subtitle_label = tk.Label(root, text="Choose an option below", font=("Helvetica", 15), foreground="#FFFFFF", background=background_color)
subtitle_label.pack()


# Load image file
icon = tk.PhotoImage(file="maze.PNG")

# Set window icon
root.iconphoto(True, icon)


def open_Astar_window():


    # Create a new window to input rows and columns
    astar_input_window = tk.Toplevel(root)
    astar_input_window.title("A Star Input")


    # Create label and entry widgets for rows and columns
    rows_label = ttk.Label(astar_input_window, text="Rows:")
    rows_label.grid(column=0, row=0, padx=5, pady=5)
    rows_entry = ttk.Entry(astar_input_window)
    rows_entry.insert(0,"0")
    
    rows_entry.grid(column=1, row=0, padx=5, pady=5)

    cols_label = ttk.Label(astar_input_window, text="Columns:")
    cols_label.grid(column=0, row=1, padx=5, pady=5)
    cols_entry = ttk.Entry(astar_input_window)
    cols_entry.insert(0,"0")

    cols_entry.grid(column=1, row=1, padx=5, pady=5)


    # Create label and entry widgets for loop
    loop_label = ttk.Label(astar_input_window, text="Loop:")
    loop_label.grid(column=0, row=2, padx=5, pady=5)
    loop_entry = ttk.Entry(astar_input_window)
    loop_entry.insert(0,"0")
    loop_entry.grid(column=1, row=2, padx=5, pady=5)

    

    # Create label and slider widgets for speed
    speed_label = ttk.Label(astar_input_window, text="Solve Speed:")
    speed_label.grid(column=0, row=3, padx=5, pady=5)
    speed_slider = ttk.Scale(astar_input_window, from_=1000, to=25, orient="horizontal")
    speed_slider.set(300)
    speed_slider.grid(column=1, row=3, padx=5, pady=5)
    

    # Create label and radio button widgets for theme
    theme_label = ttk.Label(astar_input_window, text="Theme:")
    theme_label.grid(column=0, row=4, padx=5, pady=5)
    theme_var = tk.StringVar()
    theme_var.set("light")
    light_rb = ttk.Radiobutton(astar_input_window, text="Light", variable=theme_var, value="light")
    light_rb.grid(column=1, row=4, padx=5, pady=5)
    dark_rb = ttk.Radiobutton(astar_input_window, text="Dark", variable=theme_var, value="dark")
    dark_rb.grid(column=2, row=4, padx=5, pady=5)

    # Create label and radio button widgets for maze pattern
    pattern_label = ttk.Label(astar_input_window, text="Pattern:")
    pattern_label.grid(column=0, row=5, padx=5, pady=5)
    pattern_var = tk.StringVar()
    pattern_var.set("h")
    horizontal_rb = ttk.Radiobutton(astar_input_window, text="Horizontal", variable=pattern_var, value="h")
    horizontal_rb.grid(column=1, row=5, padx=5, pady=5)
    vertical_rb = ttk.Radiobutton(astar_input_window, text="Vertical", variable=pattern_var, value="v")
    vertical_rb.grid(column=2, row=5, padx=5, pady=5)
    no_pattern = ttk.Radiobutton(astar_input_window, text="Random Pattern", variable=pattern_var, value="")
    no_pattern.grid(column=3, row=5, padx=5, pady=5)

    
    #Save maze label
    save_label = ttk.Label(astar_input_window, text="Save Maze:")
    save_label.grid(column=0, row=6, padx=5, pady=5)
    save_var = tk.BooleanVar()
    save_var.set(False)
    save_yes = ttk.Radiobutton(astar_input_window, text="Yes", variable=save_var, value=True)
    save_yes.grid(column=1, row=6, padx=5, pady=5)
    save_no = ttk.Radiobutton(astar_input_window, text="No", variable=save_var, value=False)
    save_no.grid(column=2, row=6, padx=5, pady=5)



    # Create a StringVar to store the file path
    file_path_var = tk.StringVar()

    # Create a Label widget to display the file path
    file_path_label = ttk.Label(astar_input_window, textvariable=file_path_var)
    file_path_label.grid(column=4, row=7, columnspan=3, padx=5, pady=5)

    def open_file_dialog():
        # Show a file dialog to select a file
        file_path = filedialog.askopenfilename()

        # Set the value of the file path StringVar to the selected file path
        file_path_var.set(file_path)
    

    # Create a button to open the file dialog
    load_maze_button = ttk.Button(astar_input_window, text="Load Maze", command=open_file_dialog)
    load_maze_button.grid(column=0, row=7, columnspan=3, padx=5, pady=5)

   # Create a button to submit the inputs and open the A* window
    submit_button = ttk.Button(astar_input_window, text="Submit",
                               command=lambda: open_astar_window_helper(
                                int(rows_entry.get()), 
                                int(cols_entry.get()), 
                                theme_var.get(), 
                                str(pattern_var.get()), 
                                bool(save_var.get()), 
                                int(loop_entry.get()) if loop_entry.get() else 0, 
                                file_path_var.get(),
                                int(speed_slider.get())
                                ))

    submit_button.grid(column=0, row=8, columnspan=3, padx=5, pady=5)
    
    # Create a back button to go back to the main menu window
    back_button = ttk.Button(astar_input_window, text="Back", command=astar_input_window.destroy)
    back_button.grid(column=0, row=9, columnspan=3, padx=5, pady=5)

    def open_astar_window_helper(rows, cols,theme,pattern,save,maze_loop,maze_file,speed):
        # Close the BFS input window
        astar_input_window.destroy()

        # Close the main menu window
        root.destroy()

        # Open the BFS window you've already created, passing in rows and cols as parameters

        maze_generation_time = time.time()

        #Generates a maze with the inputted rows and cols entered by user. 
        my_maze = maze(rows, cols)
        
        # Checking if a file is provided if yes load the file otherwise don't
        if maze_file:
            # Opens the maze the user selects and loads it using a predefined theme.
            my_maze.CreateMaze(theme=theme,loadMaze=maze_file)
        else:
            #Generates the maze based on the input entered which is passed to the createMaze function
            # to generate the maze the theme, patter, loop percentages and whether the maze should 
            # be saved or not
            my_maze.CreateMaze(theme=theme,pattern=pattern,loopPercent=maze_loop,saveMaze=save)
        maze_generation_end_time = time.time()
        total_time_maze = (maze_generation_end_time-maze_generation_time)
        
        start = time.time()
        search_path,came_from,path= Astar_solver.aStar(my_maze)
        end = time.time()
        elapsed_time = end - start

        
        all_path = agent(my_maze, footprints = True, color = COLOR.yellow, shape= "square",filled=True)
        solved_path = agent(my_maze,1,1 ,footprints = True, color = COLOR.green, shape= "square",filled=True,goal=(my_maze.rows,my_maze.cols))
        my_maze.tracePath({all_path:search_path}, delay=speed)
        my_maze.tracePath({solved_path:came_from},delay=speed)

        l = textLabel(my_maze, "Length of shortest Path:", len(path))
        title = textLabel(my_maze, "A* Algorithm: ")
        solve_time = textLabel(my_maze, "Time taken for Algorithm to solve:", float(elapsed_time))
        #my_maze.quit_button()

        #my_maze.create_counter_label()
        my_maze.run()



# Create a function to open the BFS window
def open_bfs_window():
    # Create a new window to input rows and columns
    bfs_input_window = tk.Toplevel(root)
    bfs_input_window.title("BFS Input")

    # Create label and entry widgets for rows and columns
    rows_label = ttk.Label(bfs_input_window, text="Rows:")
    rows_label.grid(column=0, row=0, padx=5, pady=5)
    rows_entry = ttk.Entry(bfs_input_window)
    rows_entry.insert(0,"0")
    rows_entry.grid(column=1, row=0, padx=5, pady=5)

    cols_label = ttk.Label(bfs_input_window, text="Columns:")
    cols_label.grid(column=0, row=1, padx=5, pady=5)
    cols_entry = ttk.Entry(bfs_input_window)
    cols_entry.insert(0,"0")
    cols_entry.grid(column=1, row=1, padx=5, pady=5)

    # Create label and entry widgets for loop
    loop_label = ttk.Label(bfs_input_window, text="Loop:")
    loop_label.grid(column=0, row=2, padx=5, pady=5)
    loop_entry = ttk.Entry(bfs_input_window)
    loop_entry.insert(0,"0")
    loop_entry.grid(column=1, row=2, padx=5, pady=5)


    # Create label and slider widgets for speed
    speed_label = ttk.Label(bfs_input_window, text="Solve Speed:")
    speed_label.grid(column=0, row=3, padx=5, pady=5)
    speed_slider = ttk.Scale(bfs_input_window, from_=1000, to=25, orient="horizontal")
    speed_slider.set(300)
    speed_slider.grid(column=1, row=3, padx=5, pady=5)

    # Create label and radio button widgets for theme
    theme_label = ttk.Label(bfs_input_window, text="Theme:")
    theme_label.grid(column=0, row=4, padx=5, pady=5)
    theme_var = tk.StringVar()
    theme_var.set("light")
    light_rb = ttk.Radiobutton(bfs_input_window, text="Light", variable=theme_var, value="light")
    light_rb.grid(column=1, row=4, padx=5, pady=5)
    dark_rb = ttk.Radiobutton(bfs_input_window, text="Dark", variable=theme_var, value="dark")
    dark_rb.grid(column=2, row=4, padx=5, pady=5)

    # Create label and radio button widgets for maze pattern
    pattern_label = ttk.Label(bfs_input_window, text="Pattern:")
    pattern_label.grid(column=0, row=5, padx=5, pady=5)
    pattern_var = tk.StringVar()
    pattern_var.set("h")
    horizontal_rb = ttk.Radiobutton(bfs_input_window, text="Horizontal", variable=pattern_var, value="h")
    horizontal_rb.grid(column=1, row=5, padx=5, pady=5)
    vertical_rb = ttk.Radiobutton(bfs_input_window, text="Vertical", variable=pattern_var, value="v")
    vertical_rb.grid(column=2, row=5, padx=5, pady=5)
    no_pattern = ttk.Radiobutton(bfs_input_window, text="Random Pattern", variable=pattern_var, value="")
    no_pattern.grid(column=3, row=5, padx=5, pady=5)

    #Save maze label
    save_label = ttk.Label(bfs_input_window, text="Save Maze:")
    save_label.grid(column=0, row=6, padx=5, pady=5)
    save_var = tk.BooleanVar()
    save_var.set(False)
    save_yes = ttk.Radiobutton(bfs_input_window, text="Yes", variable=save_var, value=True)
    save_yes.grid(column=1, row=6, padx=5, pady=5)
    save_no = ttk.Radiobutton(bfs_input_window, text="No", variable=save_var, value=False)
    save_no.grid(column=2, row=6, padx=5, pady=5)

    # Create a StringVar to store the file path
    file_path_var = tk.StringVar()

    # Create a Label widget to display the file path
    file_path_label = ttk.Label(bfs_input_window, textvariable=file_path_var)
    file_path_label.grid(column=4, row=7, columnspan=3, padx=5, pady=5)

    def open_file_dialog():
        # Show a file dialog to select a file
        file_path = filedialog.askopenfilename()

        # Set the value of the file path StringVar to the selected file path
        file_path_var.set(file_path)
    

    # Create a button to open the file dialog
    load_maze_button = ttk.Button(bfs_input_window, text="Load Maze", command=open_file_dialog)
    load_maze_button.grid(column=0, row=7, columnspan=3, padx=5, pady=5)

   # Create a button to submit the inputs and open the A* window
    submit_button = ttk.Button(bfs_input_window, text="Submit",
                               command=lambda: open_bfs_window_helper(
                                int(rows_entry.get()), 
                                int(cols_entry.get()), 
                                theme_var.get(), 
                                str(pattern_var.get()), 
                                bool(save_var.get()), 
                                int(loop_entry.get()) if loop_entry.get() else 0, 
                                file_path_var.get(),
                                int(speed_slider.get())
                                ))

    submit_button.grid(column=0, row=8, columnspan=3, padx=5, pady=5)

    # Create a back button to go back to the main menu window
    back_button = ttk.Button(bfs_input_window, text="Back", command=bfs_input_window.destroy)
    back_button.grid(column=0, row=9, columnspan=3, padx=5, pady=5)

    # Create a function to open the BFS window with the given dimensions
    def open_bfs_window_helper(rows, cols,theme,pattern,save,maze_loop,maze_file,speed):
        # Close the BFS input window
        bfs_input_window.destroy()

        # Close the main menu window
        root.destroy()
        my_maze = maze(rows, cols)
        
        if maze_file:
            my_maze.CreateMaze(loadMaze=maze_file)
        else:

            my_maze.CreateMaze(theme=theme,pattern=pattern,loopPercent=maze_loop,saveMaze=save)

        
        start = time.time()
        all_visited_coords, parent_coords, shortest_path = BFS_Solver.BFS(my_maze)
        end = time.time()
        elapsed_time = end - start

        #start_colour = COLOR.blue.value[1]
        a = agent(my_maze, footprints = True, color = COLOR.yellow, shape= "square",filled=True)
        c = agent(my_maze,1,1 ,footprints = True, color = COLOR.green, shape= "square",filled=True,goal=(my_maze.rows,my_maze.cols))
        
        my_maze.tracePath({a:all_visited_coords}, delay=speed)
        my_maze.tracePath({c:parent_coords}, delay = speed)

        l = textLabel(my_maze, "Length of shortest Path", len(shortest_path))
        solve_time = textLabel(my_maze, "Time taken to solve", float(elapsed_time))

        
       # my_maze.quit_button()
        
        #my_maze.create_counter_label()
        my_maze.run()






# Create a function to open the BFS window
def open_wallFollower_window():
    # Create a new window to input rows and columns
    wall_follower_input_window = tk.Toplevel(root)
    wall_follower_input_window.title("BFS Input")

    # Create label and entry widgets for rows and columns
    rows_label = ttk.Label(wall_follower_input_window, text="Rows:")
    rows_label.grid(column=0, row=0, padx=5, pady=5)
    rows_entry = ttk.Entry(wall_follower_input_window)
    rows_entry.insert(0,"0")
    rows_entry.grid(column=1, row=0, padx=5, pady=5)

    cols_label = ttk.Label(wall_follower_input_window, text="Columns:")
    cols_label.grid(column=0, row=1, padx=5, pady=5)
    cols_entry = ttk.Entry(wall_follower_input_window)
    cols_entry.insert(0,"0")
    cols_entry.grid(column=1, row=1, padx=5, pady=5)

    # Create label and entry widgets for loop
    loop_label = ttk.Label(wall_follower_input_window, text="Loop:")
    loop_label.grid(column=0, row=2, padx=5, pady=5)
    loop_entry = ttk.Entry(wall_follower_input_window)
    loop_entry.insert(0,"0")
    loop_entry.grid(column=1, row=2, padx=5, pady=5)


    # Create label and slider widgets for speed
    speed_label = ttk.Label(wall_follower_input_window, text="Solve Speed:")
    speed_label.grid(column=0, row=3, padx=5, pady=5)
    speed_slider = ttk.Scale(wall_follower_input_window, from_=1000, to=25, orient="horizontal")
    speed_slider.set(300)
    speed_slider.grid(column=1, row=3, padx=5, pady=5)

    # Create label and radio button widgets for theme
    theme_label = ttk.Label(wall_follower_input_window, text="Theme:")
    theme_label.grid(column=0, row=4, padx=5, pady=5)
    theme_var = tk.StringVar()
    theme_var.set("light")
    light_rb = ttk.Radiobutton(wall_follower_input_window, text="Light", variable=theme_var, value="light")
    light_rb.grid(column=1, row=4, padx=5, pady=5)
    dark_rb = ttk.Radiobutton(wall_follower_input_window, text="Dark", variable=theme_var, value="dark")
    dark_rb.grid(column=2, row=4, padx=5, pady=5)

    # Create label and radio button widgets for maze pattern
    pattern_label = ttk.Label(wall_follower_input_window, text="Pattern:")
    pattern_label.grid(column=0, row=5, padx=5, pady=5)
    pattern_var = tk.StringVar()
    pattern_var.set("h")
    horizontal_rb = ttk.Radiobutton(wall_follower_input_window, text="Horizontal", variable=pattern_var, value="h")
    horizontal_rb.grid(column=1, row=5, padx=5, pady=5)
    vertical_rb = ttk.Radiobutton(wall_follower_input_window, text="Vertical", variable=pattern_var, value="v")
    vertical_rb.grid(column=2, row=5, padx=5, pady=5)
    no_pattern = ttk.Radiobutton(wall_follower_input_window, text="Random Pattern", variable=pattern_var, value="")
    no_pattern.grid(column=3, row=5, padx=5, pady=5)

    #Save maze label
    save_label = ttk.Label(wall_follower_input_window, text="Save Maze:")
    save_label.grid(column=0, row=6, padx=5, pady=5)
    save_var = tk.BooleanVar()
    save_var.set(False)
    save_yes = ttk.Radiobutton(wall_follower_input_window, text="Yes", variable=save_var, value=True)
    save_yes.grid(column=1, row=6, padx=5, pady=5)
    save_no = ttk.Radiobutton(wall_follower_input_window, text="No", variable=save_var, value=False)
    save_no.grid(column=2, row=6, padx=5, pady=5)

    # Create a StringVar to store the file path
    file_path_var = tk.StringVar()

    # Create a Label widget to display the file path
    file_path_label = ttk.Label(wall_follower_input_window, textvariable=file_path_var)
    file_path_label.grid(column=4, row=7, columnspan=3, padx=5, pady=5)

    def open_file_dialog():
        # Show a file dialog to select a file
        file_path = filedialog.askopenfilename()

        # Set the value of the file path StringVar to the selected file path
        file_path_var.set(file_path)
    

    # Create a button to open the file dialog
    load_maze_button = ttk.Button(wall_follower_input_window, text="Load Maze", command=open_file_dialog)
    load_maze_button.grid(column=0, row=7, columnspan=3, padx=5, pady=5)

   # Create a button to submit the inputs and open the A* window
    submit_button = ttk.Button(wall_follower_input_window, text="Submit",
                               command=lambda: open_wall_follower_window_helper(
                                int(rows_entry.get()), 
                                int(cols_entry.get()), 
                                theme_var.get(), 
                                str(pattern_var.get()), 
                                bool(save_var.get()), 
                                int(loop_entry.get()) if loop_entry.get() else 0, 
                                file_path_var.get(),
                                int(speed_slider.get())
                                ))

    submit_button.grid(column=0, row=8, columnspan=3, padx=5, pady=5)

    # Create a back button to go back to the main menu window
    back_button = ttk.Button(wall_follower_input_window, text="Back", command=wall_follower_input_window.destroy)
    back_button.grid(column=0, row=9, columnspan=3, padx=5, pady=5)

    # Create a function to open the BFS window with the given dimensions
    def open_wall_follower_window_helper(rows, cols,theme,pattern,save,maze_loop,maze_file,speed):
        # Close the BFS input window
        wall_follower_input_window.destroy()

        # Close the main menu window
        root.destroy()
        m = maze(rows, cols)
        
        if maze_file:
            m.CreateMaze(loadMaze=maze_file)
        else:

            m.CreateMaze(theme=theme,pattern=pattern,loopPercent=maze_loop,saveMaze=save)

        
        start = time.time()
        path,path2 = wallFollower_solver.wall_follower(m)
        end = time.time()
        elapsed_time = end - start

        a=agent(m,shape='arrow',footprints=False)
            
        m.tracePath({a:path},delay=speed)
        
        generate_txt_file(path)
        #l = textLabel(m, "Path Followed is: ", str(path))
        solve_time = textLabel(m, "Time taken to solve", float(elapsed_time))
        print(path)
        #m.quit_button()
        #m.create_counter_label()
        m.run()


def generate_txt_file(value):
    with open("path_taken.txt", "w") as file:
        file.write("The Path this algorithm follows on this maze is: " + "'" + value + "' " )




# Define a custom style for rounded buttons
root.style = ttk.Style()
root.style.configure('Rounded.TButton', borderwidth=0, padding=6, relief='flat', background='dark orange', font=('Arial', 12, 'bold'), foreground=background_color)
root.style.map('Rounded.TButton', background=[('active', '#98FB98')])

# Define buttons for solving a maze using various algorithms
bfs_button = ttk.Button(root, text="BFS Solver", command=open_bfs_window, style='Rounded.TButton')
astar_button = ttk.Button(root, text="A* Solver", command=open_Astar_window, style='Rounded.TButton')
wall_follower_button = ttk.Button(root, text="Wall Follower Solver", command=open_wallFollower_window, style='Rounded.TButton')

# Pack the buttons into the GUI with some padding
bfs_button.pack(pady=(20,10))
astar_button.pack(pady=10)
wall_follower_button.pack(pady=10)

# Create a button to quit the program
quit_button = ttk.Button(root, text="Quit", command=root.quit, style='Rounded.TButton')
quit_button.pack(pady=(20,0))


# Start the main loop
root.mainloop()
