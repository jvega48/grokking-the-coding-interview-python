# brute force solution n^2
import math
# Problem Statement #
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any 
# contiguous subarray of size ‘k’.

def max_window_sum_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)

    return max_sum

# efficient solution 0(N) 
def max_window_sum_of_size_k_efficient(k, arr):
    max_sum , window_sum = 0, 0
    window_start = 0

    for windowEnd in range(len(arr)):
        window_sum += arr[windowEnd]

        if windowEnd >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


print(max_window_sum_of_size_k_efficient(2, [2,3,4,1,5]))

# Problem Statement #
# Given an array of positive numbers and a positive number ‘S’, find the 
# length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.

def smallest_subarayy_with_given_sum(sum, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]

        while window_sum >= sum:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
            return 0

    return min_length

print(smallest_subarayy_with_given_sum(8, [3,4,1,1,6]))

# Problem Statement #
# Given a string, find the length of the longest substring in it
# with no more than K distinct characters.

def longest_substring_with_k_distinct(strr, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(strr)):
        char = strr[window_end]

        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

        while len(char_frequency) > k:
            char_left =  strr[window_start]
            char_frequency[char_left] -= 1

            if char_frequency[char_left] == 0:
                del char_frequency[char_left]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

print(longest_substring_with_k_distinct("araaci", 2))

# Given an array of characters where each character represents a 
# fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t 
# skip a tree. You will pick one fruit from each tree until you cannot, 
# i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the 
# baskets.

def fruits_into_basket(fruits):
    window_start = 0
    max_length_trees = 0
    tree_frequency = { }

    for windown_end in range(len(fruits)):
        fruit = fruits[windown_end]

        if fruit not in tree_frequency:
            tree_frequency[fruit] = 0
        tree_frequency[fruit] += 1

        while len(tree_frequency) > 2:
            starting_tree = fruits[window_start]
            tree_frequency[starting_tree] -= 1
            if tree_frequency[starting_tree] == 0:
                del tree_frequency[starting_tree] 
            window_start += 1
        
        max_length_trees = max(max_length_trees, windown_end - window_start + 1)

    return max_length_trees


print(fruits_into_basket(['S','B','S','V','I','S']))