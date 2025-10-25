"""
Challenge 3: Container With Most Water

Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The max area of water the container can contain is 49.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Approach:
Use two pointers technique starting from both ends and move the pointer with smaller height.
"""

def max_area(height):
    """
    Find the maximum area between two lines in the array.
    
    Args:
        height (List[int]): Array representing heights of vertical lines
        
    Returns:
        int: Maximum area that can be stored
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    print(f"Heights: {height1} -> Max area: {max_area(height1)}")
    
    # Test case 2
    height2 = [1,1]
    print(f"Heights: {height2} -> Max area: {max_area(height2)}")
    
    # Additional test case
    height3 = [4,3,2,1,4]
    print(f"Heights: {height3} -> Max area: {max_area(height3)}")