# Directions: [up, down, left, right]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def max_light_loop(M, N, grid):
    def in_bounds(x, y):
        return 0 <= x < M and 0 <= y < N
    
    def get_new_direction(x, y, direction):
        if grid[x][y] == '/':
            if direction == 0:  # up -> right
                return 3
            if direction == 1:  # down -> left
                return 2
            if direction == 2:  # left -> down
                return 1
            if direction == 3:  # right -> up
                return 0
        elif grid[x][y] == '\\':
            if direction == 0:  # up -> left
                return 2
            if direction == 1:  # down -> right
                return 3
            if direction == 2:  # left -> up
                return 0
            if direction == 3:  # right -> down
                return 1
        return direction  # no change if it's a '0' cell
    
    def trace_path(start_x, start_y, start_dir):
        visited = set()  # to track visited cells
        x, y, dir = start_x, start_y, start_dir
        path = []  # to store the path taken
        
        while in_bounds(x, y) and (x, y, dir) not in visited:
            visited.add((x, y, dir))
            path.append((x, y))
            dir = get_new_direction(x, y, dir)
            x += directions[dir][0]
            y += directions[dir][1]
        
        if (x, y, dir) in visited:
            return len(path)  # we found a loop and return the loop size
        return 0  # no loop
        
    max_cells = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] in ['/','\\']:  # only start at mirror positions
                for start_dir in range(4):  # Try all four possible directions
                    max_cells = max(max_cells, trace_path(i, j, start_dir))
    
    return max_cells

# Input Parsing
M, N = map(int, input().split())  # Grid size M rows, N columns
grid = [input().split() for _ in range(M)]  # Grid structure

# Function call to calculate max loop size
result = max_light_loop(M, N, grid)
print(result)
