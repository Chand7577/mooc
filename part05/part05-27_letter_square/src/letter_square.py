
number=int(input())
size=(2*number)-1    
    # Generate the square
for row in range(size):
    current_row = []
    for col in range(size):
            # Find the minimum of row and col distances to the center
        row_dist = abs(row - (size//2))
        col_dist = abs(col - (size//2))
            
            
            # Use the maximum of these distances to determine the letter
        layer = max(row_dist, col_dist)
            
            # Convert layer to letter
        current_letter = chr(ord('A') + layer)
        current_row.append(current_letter)
        
        # Print the row
    print(''.join(current_row))
