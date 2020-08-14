"""
Leetcode: 953. Verifying an Alien Dictionary

Attempts: 1
Completed: Y
Acheived Ideal: Yes

Time Complexity: O(n * k)
Space Complexity: O(1)

Pattern: Array Question with dictionary Lookup
Technique: 

Problems Encountered:
Other Solutions:

"""


'''
Requirements: - Check if the words in array(words) are lexixographically sorted in
                the alien language.
            - When comparing two words, check if second is word letter comes after
                the first word letter. If they are the same, check the next letter
            - If one word is shorter than the other and they are identical to each                      other up to the end of the shorter word -> the shorter one comes                      first

Process: 
- Check if words is None => False
- check if words length is one => True 
- Generate a dictionary with the char:index 
- For loop that would iterate once on words
- store min length of both words
- Loop though minlength comparing each char and make sure that second word char >= first word char
- If firstword length > secondword length => return False
- return True

Time: O(n * k ) where k=maxLengthOfWord
Space: O(1)

["word","world","row"]
'''


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        if len(words) == 1:
            return True
        alphabet = {}
        for index, char in enumerate(order):
            alphabet[char] = index

        for i in range(0, len(words)-1):
            firstWord = words[i]
            secondWord = words[i+1]
            minLength = min(len(firstWord), len(secondWord))
            for j in range(0, minLength):
                firstChar = alphabet[firstWord[j]]
                secondChar = alphabet[secondWord[j]]
                if secondChar > firstChar:
                    break
                elif secondChar < firstChar:
                    return False
                if j == (minLength-1) and len(secondWord) < len(firstWord):
                    return False
        return True
