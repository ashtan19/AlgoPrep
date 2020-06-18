'''
Question: Triplet Sum to Zero (medium)

Time Complexity: O(n^2)
Space Complexity: O(n)

Pattern: Two Pointer
Technique: Three Pointers. Sort array. Iterate through array from front to back. Use Pair With Target Sum to find
            the negative of current value in the rest of the array. Make sure to find all pairs in 
            one iteration
'''


def search_triplets(arr):
    triplets = []

    def pair_with_targetsum(arr, target_sum, left, triplets):
        front = left
        end = len(arr) - 1
        while front < end:
            curr_sum = arr[front] + arr[end]
            if curr_sum == target_sum:
                triplets.append([-target_sum, arr[front], arr[end]])
                front += 1
                end -= 1
                while left < end and arr[front] == arr[front-1]:
                    front += 1
                while left < end and arr[end] == arr[end+1]:
                    end -= 1
            elif curr_sum < target_sum:
                front += 1
            else:
                end -= 1

        return

        # TODO: Write your code here
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        pair_with_targetsum(arr, -arr[i], i+1, triplets)

    return triplets
