"""
Question: Frequency Sort

Time Complexity: O(nlogn)
Space Complexity: O(n)

Pattern: Top K Elements 
Technique: Use a Frequency hash table

"""


from heapq import *
from collections import Counter


def sort_character_by_frequency(str):
    # TODO: Write your code here
    freq_table = Counter(str)
    max_heap = []
    result = ""

    for char, frequency in freq_table.items():
        heappush(max_heap, (-frequency, char))

    while max_heap:
        frequency, char = heappop(max_heap)
        for _ in range(-frequency):
            result = result + char

    return result

