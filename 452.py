def find_min_arrows(points):
    if not points:
        return 0
    
    # Sort balloons based on their ending points
    points.sort(key=lambda x: x[1])
    
    arrows = 1  # Initialize the number of arrows to 1
    end = points[0][1]  # Initialize the ending point of the first balloon
    
    # Iterate through the sorted balloons
    for start, curr_end in points[1:]:
        # If the current balloon starts after the ending point of the previous balloon
        if start > end:
            arrows += 1
            end = curr_end  # Update the ending point
        
    return arrows

# Example usage
points = [[10,16],[2,8],[1,6],[7,12]]
result = find_min_arrows(points)
print(result)  # Output: 2
