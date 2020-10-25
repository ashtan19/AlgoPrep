"""
Leetcode: Amazon OA Cut Off Rank

Attempts: 1
Completed: Y
Acheived Ideal: Meh
Under 30 Mins: Y

Time Complexity: O(nlogn) because of sorting. Can be O(n)
Space Complexity:

Pattern: 
Technique: 

Problems Encountered:
Other Solutions:

"""


def numLevelUp(cutOffRank, num, scores):
    scores.sort(reverse=True)

    seen_scores = {}
    num_levelers = 0

    for i in range(len(scores)):
        if len(seen_scores) <= cutOffRank:
            score = scores[i]
            if score == 0:
                return num_levelers
            if score not in seen_scores:
                if num_levelers >= cutOffRank:
                    return num_levelers
                seen_scores[score] = True
            num_levelers += 1
        else:
            break

    return num_levelers


print(numLevelUp(3, 4, [100, 50, 50, 25]))
print(numLevelUp(4, 5, [2, 2, 3, 4, 5]))
