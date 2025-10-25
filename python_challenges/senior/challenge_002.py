"""
Challenge 2: Word Ladder

Problem Description:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog"

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

Approach:
Use BFS to find the shortest transformation sequence.
"""

from collections import deque

def ladder_length(begin_word, end_word, word_list):
    """
    Find the length of the shortest transformation sequence from begin_word to end_word.
    
    Args:
        begin_word (str): Starting word
        end_word (str): Target word
        word_list (List[str]): List of valid words
        
    Returns:
        int: Number of words in shortest transformation sequence, or 0 if no such sequence exists
    """
    # Your implementation here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1
    begin_word1 = "hit"
    end_word1 = "cog"
    word_list1 = ["hot","dot","dog","lot","log","cog"]
    print(f"Begin: {begin_word1}, End: {end_word1}")
    print(f"Word list: {word_list1}")
    print(f"Transformation length: {ladder_length(begin_word1, end_word1, word_list1)}")
    
    # Test case 2
    begin_word2 = "hit"
    end_word2 = "cog"
    word_list2 = ["hot","dot","dog","lot","log"]
    print(f"\nBegin: {begin_word2}, End: {end_word2}")
    print(f"Word list: {word_list2}")
    print(f"Transformation length: {ladder_length(begin_word2, end_word2, word_list2)}")