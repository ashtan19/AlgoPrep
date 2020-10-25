"""
Leetcode: Amazon OA Count Teams

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: 
Space Complexity:

Pattern: 
Technique: 

Problems Encountered: Need the combinations fomula or use the itertools combinations method
Other Solutions:

"""


import math as math
from itertools import combinations


def CountTeams(skills, minAssociates, minLevel, maxLevel):
    def inSkillRange(skill):
        return skill >= minLevel and skill <= maxLevel

    valid_workers = filter(inSkillRange, skills)
    n = len(valid_workers)

    if n < minAssociates:
        return 0

    result = []
    for r in range(minAssociates, n+1):
        comb = combinations(valid_workers, r)
        result += comb

    return len(result)


print(CountTeams([12, 4, 6, 13, 5, 10], 3, 4, 10))  # 5
print(CountTeams([1, 2, 3, 4, 5, 10], 3, 1, 10))  # 42
print(CountTeams([12, 4, 6, 13, 5, 10], 3, 5, 15))  # 16
print(CountTeams([1, 2, 3, 4, 5, 10], 6, 1, 10))  # 1
print(CountTeams([1, 2, 3, 4, 5, 10], 5, 1, 10))  # 7
