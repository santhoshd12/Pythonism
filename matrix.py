def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    N = int(data[index])
    index += 1
    
    r, c = map(int, data[index].split())
    index += 1
    
    matrices = []
    flat_matrix_data = list(map(int, ' '.join(data[index:index+r]).split()))
    index += r
    
    # Split the flat matrix data into individual matrices
    for i in range(N):
        matrix = []
        for j in range(r):
            start = (i * r * c) + (j * c)
            end = start + c
            matrix.append(flat_matrix_data[start:end])
        matrices.append(matrix)
    
    instructions = []
    while index < len(data):
        instructions.append(list(map(int, data[index].split())))
        index += 1
    
    for instruction in instructions:
        for matrix_index in instruction:
            for row in matrices[matrix_index - 1]:  
                print(" ".join(map(str, row)))

main()
