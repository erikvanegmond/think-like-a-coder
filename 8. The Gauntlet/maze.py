from itertools import count
import random

class Node(object):
    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)

    def reset(self):
        self._ids = count(0)
        
class Maze:
    def __init__(self, depth=10):
        self.depth = depth
        self.exit_num = random.randint(0,2**(depth)-1)
        self.n_leaves = 0
        self.maze = self.gen_maze()
        
    def __repr__(self):
        return str(self.maze) 
    
    def items(self):
        return self.maze.items()
    
    def gen_maze(self, depth=None, my_id=None):
        if depth == None:
            depth = self.depth
        if depth:
            id1 = Node().id
            id2 = Node().id
            maze = {"left": self.gen_maze(depth-1, id1),
                    "right": self.gen_maze(depth-1, id2)}
        else:
            if self.n_leaves == self.exit_num:
                maze="exit"
            else:
                maze = "end"
            self.n_leaves+=1
        return maze
    
    def walk(self, path):
        to_walk = self.maze
        for step in path:
            to_walk = to_walk[step]
        if to_walk == "exit":
            print(f"Ethic reached the exit safely")
        else:
            print("Ethic reached certain death")
    
    @staticmethod
    def _solve(maze):
        for current_node, sub_maze in maze.items():
            if sub_maze == "exit":
                return [current_node]
            elif sub_maze == 'end':
                continue
            else:
                answer = hedge(sub_maze)
                if answer:
                    return [current_node]+ answer
            
Node.reset(Node)
maze = Maze(10)