"""
Challenge 5: Merge Intervals

Problem Description:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

Approach:
Sort intervals by start time, then merge overlapping intervals in a single pass.
"""

def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Args:
        intervals (List[List[int]]): List of intervals [start, end]
        
    Returns:
        List[List[int]]: Merged non-overlapping intervals
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Intervals: {intervals1} -> Merged: {merge_intervals(intervals1)}")
    
    # Test case 2
    intervals2 = [[1,4],[4,5]]
    print(f"Intervals: {intervals2} -> Merged: {merge_intervals(intervals2)}")
    
    # Additional test case
    intervals3 = [[1,4],[0,4]]
    print(f"Intervals: {intervals3} -> Merged: {merge_intervals(intervals3)}")