# Time Complexity: O(n)
# Space Complexity: O(n)

# Technique: Sliding Variable Window


def longest_substring_with_k_distinct(str, k):
    # TODO: Write your code here
    result = 0
    start = 0
    hashtable = {}
    currlength = 0
    for character in str:
        hashtable[character] = hashtable.get(character, 0) + 1
        currlength += 1
        if hashtable[character] <= k:
            result = max(result, currlength-1)
        if hashtable[character] > k:
            while hashtable[character] > k:
                hashtable[str[start]] -= 1
                start += 1
                currlength -= 1

    return result
