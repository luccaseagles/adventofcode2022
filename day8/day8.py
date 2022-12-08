import numpy as np

def is_visible_in_line(line, i):
    
    if i == 0 or i == len(line)-1:
        return True
    
    height = line[i]
    before = line[:i]
    after = line[i+1:]
    if max(before) >= height and max(after) >= height:
        return False
    return True



is_visible_in_line([3,0,3,7,2], 3)

with open("input", "r") as f:
    lines = f.readlines()
    grid = [[*l.strip()] for l in lines]
    grid = [[int(el) for el in row ] for row in grid]
    forest = np.array(grid)
    n_rows, n_cols = forest.shape 
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            height = forest[i,j]
            hori_vis = is_visible_in_line(forest[:,j], i) 
            vert_vis = is_visible_in_line(forest[i,:], j) 
            if hori_vis or vert_vis:
                count += 1
    print(count)
        

