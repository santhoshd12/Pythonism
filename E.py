def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    N = int(data[0])
    sticks = []
    for i in range(1, N + 1):
        x1, y1, x2, y2 = map(int, data[i].split())
        sticks.append((x1, y1, x2, y2))
    
    # Step 1: Detect if a closed figure is formed
    from collections import defaultdict, deque
    import math
    
    def check_closed_figure(sticks):
        # Create graph
        graph = defaultdict(list)
        for x1, y1, x2, y2 in sticks:
            graph[(x1, y1)].append((x2, y2))
            graph[(x2, y2)].append((x1, y1))
        
        # Check if graph contains a cycle
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and dfs(neighbor, node):
                    return True
            return False
        
        for node in graph:
            if node not in visited:
                if dfs(node, None):
                    return True, graph
        return False, None
    
    # Step 2: If closed figure is formed, calculate area
    def calculate_area(polygon):
        n = len(polygon)
        area = 0.0
        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]
            area += (x1 * y2 - x2 * y1)
        return abs(area) / 2.0
    
    closed_figure_formed, graph = check_closed_figure(sticks)
    
    if closed_figure_formed:
        print("Yes")
        
        # Extract the closed figure from the graph
        polygon = []
        visited = set()
        stack = deque([next(iter(graph))])
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            polygon.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        area = calculate_area(polygon)
        
        # Check if Arjun can form the same figure with the leftover sticks
        leftover_sticks = []
        for stick in sticks:
            if (stick[0], stick[1]) not in polygon or (stick[2], stick[3]) not in polygon:
                leftover_sticks.append(stick)
        
        total_stick_length = sum(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) for x1, y1, x2, y2 in sticks)
        closed_figure_perimeter = sum(math.sqrt((polygon[i][0] - polygon[i-1][0]) ** 2 + (polygon[i][1] - polygon[i-1][1]) ** 2) for i in range(len(polygon)))
        
        can_form_same_figure = total_stick_length - closed_figure_perimeter >= closed_figure_perimeter
        print("Yes" if can_form_same_figure else "No")
        print(f"{area:.2f}")
    else:
        print("No")

if __name__ == "__main__":
    main()
