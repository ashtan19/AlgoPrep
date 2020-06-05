# Leetcode: 528. Random Pick with Weight

# Attempts: 1
# Completed: Y
# Acheived Ideal: N

# Time Complexity:
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Use Binary Search


# Attempt 1
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        totalweight = sum(w)
        print(w)
        print(totalweight)
        self.weightprob = []
        for weight in w:
            self.weightprob.append(float(weight)/float(totalweight))
        for i in range(1, len(self.weightprob)):
            self.weightprob[i] = self.weightprob[i] + self.weightprob[i-1]
        print(self.weightprob)

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.uniform(0, 1)
        print(rand)
        for i, prob in enumerate(self.weightprob):
            if rand <= prob:
                return i
