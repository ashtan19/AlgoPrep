# Leetcode: 380. Insert Delete GetRandom O(1)

# Attempts: 1
# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(1)
# Space Complexity: O(n)

# Solving process:
# Problems Encountered:

# Other Solutions: Could use a list as well


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomset = {}
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomset:
            return False
        else:
            self.randomset[val] = True
            self.length += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomset:
            del self.randomset[val]
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randIndex = random.randint(0, self.length-1)

        return self.randomset.keys()[randIndex]
