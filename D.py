def solve(Q, queries):
    # Dictionary to store positions of cubes
    positions = {}
    
    # Processing each query
    for cubeA, cubeB, direction in queries:
        cubeA, cubeB = int(cubeA), int(cubeB)
        
        # Ensure cubeA has a position
        if cubeA not in positions:
            positions[cubeA] = (0, 0)  # Start cubeA at (0, 0) if not already placed
        
        xA, yA = positions[cubeA]
        
        # Based on the direction, update the position of cubeB
        if direction == 'right':
            positions[cubeB] = (xA, yA + 1)
        elif direction == 'left':
            positions[cubeB] = (xA, yA - 1)
        elif direction == 'top':
            positions[cubeB] = (xA - 1, yA)
        elif direction == 'down':
            positions[cubeB] = (xA + 1, yA)
    
    # Now, count the number of common sides
    common_sides = 0
    
    # Set of positions for quick look-up
    position_set = set(positions.values())
    
    # Check adjacent cubes for common sides
    for cubeA, (xA, yA) in positions.items():
        # Check the 4 possible directions (left, right, up, down)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (xA + dx, yA + dy)
            if neighbor in position_set:
                common_sides += 1
    
    # Since each common side is counted twice, divide by 2
    return common_sides // 2

# Input parsing
Q = int(input())
queries = [input().split() for _ in range(Q)]

# Output the result
print(solve(Q, queries))
