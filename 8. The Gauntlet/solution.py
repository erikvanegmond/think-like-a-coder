from maze import maze

def hedge(maze):
    for current_node, sub_maze in maze.items():
        if sub_maze == "exit":
            return [current_node]
        elif sub_maze == 'end':
            continue
        else:
            answer = hedge(sub_maze)
            if answer:
                return [current_node] + answer
    
steps = hedge(maze)
print(maze.walk(steps))