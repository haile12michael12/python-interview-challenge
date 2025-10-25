"""
Script to generate multiple Python challenges based on templates.
"""

import os
import shutil

def generate_intermediate_challenges(start_num, count):
    """Generate intermediate level challenges."""
    intermediate_dir = "intermediate"
    template_file = "challenge_template.py"
    
    if not os.path.exists(intermediate_dir):
        os.makedirs(intermediate_dir)
    
    # Sample challenge titles and descriptions for intermediate level
    intermediate_challenges = [
        ("Two Sum", "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."),
        ("Palindrome Number", "Given an integer x, return true if x is a palindrome, and false otherwise."),
        ("Roman to Integer", "Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Convert a roman numeral to an integer."),
        ("Valid Parentheses", "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."),
        ("Merge Two Sorted Lists", "You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list."),
        ("Remove Duplicates from Sorted Array", "Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once."),
        ("Remove Element", "Given an integer array nums and an integer val, remove all occurrences of val in nums in-place."),
        ("Search Insert Position", "Given a sorted array of distinct integers and a target value, return the index if the target is found."),
        ("Maximum Subarray", "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum."),
        ("Length of Last Word", "Given a string s consisting of words and spaces, return the length of the last word in the string."),
        ("Plus One", "Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer."),
        ("Add Binary", "Given two binary strings a and b, return their sum as a binary string."),
        ("Sqrt(x)", "Given a non-negative integer x, compute and return the square root of x."),
        ("Climbing Stairs", "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"),
        ("Remove Duplicates from Sorted List", "Given the head of a sorted linked list, delete all duplicates such that each element appears only once."),
        ("Same Tree", "Given the roots of two binary trees p and q, write a function to check if they are the same or not."),
        ("Symmetric Tree", "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."),
        ("Maximum Depth of Binary Tree", "Given the root of a binary tree, return its maximum depth."),
        ("Convert Sorted Array to Binary Search Tree", "Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree."),
        ("Balanced Binary Tree", "Given a binary tree, determine if it is height-balanced."),
        ("Minimum Depth of Binary Tree", "Given a binary tree, find its minimum depth."),
        ("Path Sum", "Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum."),
        ("Pascal's Triangle", "Given an integer numRows, return the first numRows of Pascal's triangle."),
        ("Best Time to Buy and Sell Stock", "You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you can achieve."),
        ("Single Number", "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.")
    ]
    
    for i in range(count):
        challenge_num = start_num + i
        filename = f"challenge_{challenge_num:03d}.py"
        filepath = os.path.join(intermediate_dir, filename)
        
        # Use existing challenges if we've exhausted our sample list
        title, description = intermediate_challenges[i % len(intermediate_challenges)]
        
        # Create challenge content
        content = f'''"""
Challenge {challenge_num}: {title}

Problem Description:
{description}

Example:
Input: {{example input}}
Output: {{example output}}

Constraints:
{{List of constraints}}

Approach:
{{Hints about approach}}
"""

def solution_function(params):
    """
    Implementation for {title}.
    
    Args:
        params ({{type}}): {{Description of parameters}}
        
    Returns:
        {{return_type}}: {{Description of return value}}
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test cases will be added here
    pass
'''
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Generated {filepath}")

def generate_senior_challenges(start_num, count):
    """Generate senior level challenges."""
    senior_dir = "senior"
    template_file = "challenge_template.py"
    
    if not os.path.exists(senior_dir):
        os.makedirs(senior_dir)
    
    # Sample challenge titles and descriptions for senior level
    senior_challenges = [
        ("Binary Tree Maximum Path Sum", "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them."),
        ("Word Break", "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words."),
        ("LRU Cache", "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache."),
        ("Trapping Rain Water", "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining."),
        ("Best Time to Buy and Sell Stock", "You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you can achieve."),
        ("Course Schedule", "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Return true if you can finish all courses."),
        ("Design Twitter", "Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets."),
        ("Minimum Window Substring", "Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t is included."),
        ("Median of Two Sorted Arrays", "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays."),
        ("Regular Expression Matching", "Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'."),
        ("Merge k Sorted Lists", "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list."),
        ("Largest Rectangle in Histogram", "Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram."),
        ("Binary Tree Inorder Traversal", "Given the root of a binary tree, return the inorder traversal of its nodes' values."),
        ("Validate Binary Search Tree", "Given the root of a binary tree, determine if it is a valid binary search tree (BST)."),
        ("Construct Binary Tree from Preorder and Inorder Traversal", "Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree."),
        ("Next Permutation", "A permutation of an array of integers is an arrangement of its members into a sequence or linear order. The next permutation of an array is the next lexicographically greater permutation."),
        ("Search in Rotated Sorted Array", "There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k."),
        ("Find First and Last Position of Element in Sorted Array", "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value."),
        ("Combination Sum", "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target."),
        ("Jump Game", "You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position."),
        ("Permutations", "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."),
        ("Rotate Image", "You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise)."),
        ("Group Anagrams", "Given an array of strings strs, group the anagrams together. You can return the answer in any order."),
        ("Maximum Product Subarray", "Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.")
    ]
    
    for i in range(count):
        challenge_num = start_num + i
        filename = f"challenge_{challenge_num:03d}.py"
        filepath = os.path.join(senior_dir, filename)
        
        # Use existing challenges if we've exhausted our sample list
        title, description = senior_challenges[i % len(senior_challenges)]
        
        # Create challenge content
        content = f'''"""
Challenge {challenge_num}: {title}

Problem Description:
{description}

Example:
Input: {{example input}}
Output: {{example output}}

Constraints:
{{List of constraints}}

Approach:
{{Hints about approach}}
"""

def solution_function(params):
    """
    Implementation for {title}.
    
    Args:
        params ({{type}}): {{Description of parameters}}
        
    Returns:
        {{return_type}}: {{Description of return value}}
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test cases will be added here
    pass
'''
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Generated {filepath}")

if __name__ == "__main__":
    # Generate intermediate challenges 31-50
    generate_intermediate_challenges(31, 20)
    
    # Generate senior challenges 31-50
    generate_senior_challenges(31, 20)
    
    print("Challenge generation complete!")