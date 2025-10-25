"""
Challenge 4: 3Sum

Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Approach:
Sort the array and use two pointers technique for each element as the first element of triplet.
"""

def three_sum(nums):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums (List[int]): Input array of integers
        
    Returns:
        List[List[int]]: List of unique triplets that sum to zero
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1,0,1,2,-1,-4]
    print(f"Array: {nums1} -> Triplets: {three_sum(nums1)}")
    
    # Test case 2
    nums2 = [0,1,1]
    print(f"Array: {nums2} -> Triplets: {three_sum(nums2)}")
    
    # Test case 3
    nums3 = [0,0,0]
    print(f"Array: {nums3} -> Triplets: {three_sum(nums3)}")