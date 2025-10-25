"""
Challenge 1: Array Rotation

Problem Description:
Given an array of integers and a number k, rotate the array to the right by k steps.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Constraints:
- 1 <= nums.length <= 10^5
- -1000 <= nums[i] <= 1000
- 0 <= k <= 10^5

Follow-up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

def rotate_array(nums, k):
    """
    Rotate the array to the right by k steps.
    
    Args:
        nums (List[int]): The input array
        k (int): Number of steps to rotate
        
    Returns:
        List[int]: The rotated array
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    print(f"Original: {nums1}")
    print(f"Rotated by {k1}: {rotate_array(nums1.copy(), k1)}")
    
    # Test case 2
    nums2 = [-1,-100,3,99]
    k2 = 2
    print(f"Original: {nums2}")
    print(f"Rotated by {k2}: {rotate_array(nums2.copy(), k2)}")