'''
Question: 8. String to Integer (atoi)

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: 
Technique: 

'''

'''
Algorithm:
1) Trim the whitespace
2) Check the first char for + or - or if not a number => return 0
3) Iterate until we get to end of numbers
4) convert that array into a string then into a number
5) If number is greater than Int_Min return intmin
'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        print(str)
        str = str.strip()
        numString = []
        sign = ''
        index = 0
        num = 0
        if str == "":
            return 0
        if str[0] == "+" or str[0] == "-":
            sign = str[0]
            index = 1
        if index >= len(str) or ord(str[index]) < ord('0') or ord(str[index]) > ord("9"):
            return 0

        while index < len(str):
            if ord(str[index]) >= ord('0') and ord(str[index]) <= ord("9"):
                numString.append(str[index])
                index += 1
            else:
                break
        if len(numString) > 0:
            num = int("".join(numString))
        if sign == "-":
            num *= -1
        if num >= 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31

        return num
