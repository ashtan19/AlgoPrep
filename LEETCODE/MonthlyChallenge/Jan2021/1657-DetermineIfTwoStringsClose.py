"""
Leetcode:1657. Determine if Two Strings Are Close

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1) b/c there are only 26 chars and max size of hashmaps is 26

Pattern: String Manipulation
Technique: Need to find out that the solution to this question is checking if number 
            of each char frequencies are the same

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter, defaultdict

        if len(word1) != len(word2):
            return False

        char_table1 = Counter(word1)
        char_table2 = Counter(word2)

        if set(char_table1.keys()) != set(char_table2.keys()):
            print("error1")
            return False

        count_table1 = defaultdict(int)
        count_table2 = defaultdict(int)

        for count in char_table1.values():
            count_table1[count] += 1

        for count in char_table2.values():
            count_table2[count] += 1

        for count, num in count_table1.items():
            if count_table2[count] != num:
                print("error3")
                return False

        return True
