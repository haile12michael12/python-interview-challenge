"""
Challenge 2: Longest Substring Without Repeating Characters

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Approach:
Use sliding window technique with a hash map to track character positions.
"""

def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of longest substring without repeating characters
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"String: '{s1}' -> Length: {length_of_longest_substring(s1)}")
    
    # Test case 2
    s2 = "bbbbb"
    print(f"String: '{s2}' -> Length: {length_of_longest_substring(s2)}")
    
    # Test case 3
    s3 = "pwwkew"
    print(f"String: '{s3}' -> Length: {length_of_longest_substring(s3)}")
    
    # Edge case
    s4 = ""
    print(f"String: '{s4}' -> Length: {length_of_longest_substring(s4)}")