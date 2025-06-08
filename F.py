def solve(N, cards):
    # Store all card positions in a set for fast lookups
    card_positions = set()
    
    # Process the input and map each card to its corresponding set of coordinates
    for x, y, z, plane in cards:
        x, y, z = int(x), int(y), int(z)
        
        # Determine the coordinates that each card covers based on the plane
        if plane == "xy":
            card_positions.add((x, y, z, plane))
        elif plane == "yz":
            card_positions.add((x, y, z, plane))
        elif plane == "xz":
            card_positions.add((x, y, z, plane))

    # Initialize bounds to extreme values
    min_x = min_y = min_z = float('inf')
    max_x = max_y = max_z = float('-inf')
    
    # Determine the bounds of the box
    for x, y, z, _ in card_positions:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

    # Calculate the volume of the potential box
    volume = (max_x - min_x + 1) * (max_y - min_y + 1) * (max_z - min_z + 1)

    # Check all positions in the bounding box for missing cards
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) not in card_positions:
                    # If any position is missing, print the missing card's coordinates
                    print(f"{x} {y} {z} xy")  # You can adjust the plane as needed
                    return

    # If no missing card, print the volume
    print(volume)


# Input handling
def main():
    N = int(input("Enter the number of cards: "))
    cards = []
    
    # Input each card's details
    for _ in range(N):
        x, y, z, plane = input("Enter card details (x y z plane): ").split()
        cards.append((x, y, z, plane))
    
    # Call the solve function with the user input
    solve(N, cards)

# Run the program
main()
