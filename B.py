directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right

def in_bounds(x, y, M, N):
    return 0 <= x < M and 0 <= y < N

def get_new_direction(x, y, direction, grid):
    if grid[x][y] == '/':
        if direction == 0:  # up
            return 3  # right
        elif direction == 1:  # down
            return 2  # left
        elif direction == 2:  # left
            return 1  # down
        elif direction == 3:  # right
            return 0  # up
    elif grid[x][y] == '\\':
        if direction == 0:  # up
            return 2  # left
        elif direction == 1:  # down
            return 3  # right
        elif direction == 2:  # left
            return 0  # up
        elif direction == 3:  # right
            return 1  # down
    return direction  # if no mirror, keep direction the same

def trace_path(start_x, start_y, start_dir, M, N, grid):
    visited = set()  # To store the visited cells to detect loops
    x, y, dir = start_x, start_y, start_dir
    path = []  # List to store the cells in the path
    
    while in_bounds(x, y, M, N) and (x, y, dir) not in visited:
        visited.add((x, y, dir))
        path.append((x, y))  # Add the current cell to the path
        dir = get_new_direction(x, y, dir, grid)  # Change the direction based on the mirror
        x += directions[dir][0]  # Move to the next cell based on direction
        y += directions[dir][1]
    
    if (x, y, dir) in visited:
        return len(path)  # If we revisit a cell, return the length of the path (loop length)
    return 0  # No loop found

def max_light_loop(M, N, grid):
    max_cells = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] in ['/', '\\']:  # Only start tracing from mirrors
                for start_dir in range(4):  # Try all four directions (up, down, left, right)
                    max_cells = max(max_cells, trace_path(i, j, start_dir, M, N, grid))
    
    return max_cells

M, N = map(int, input().split())  # Read M and N
grid = [input().split() for _ in range(M)]  # Read the grid structure

result = max_light_loop(M, N, grid)
print(result)  # Output the result
