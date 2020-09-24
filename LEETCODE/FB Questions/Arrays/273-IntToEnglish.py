"""
Leetcode: 273. Integer to English Words

Attempts: 1
Completed: Y
Acheived Ideal: Yes but very bad code
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: 
Technique: 

Problems Encountered:
Other Solutions:

"""

# Cleaner Solution


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result


# My first solution
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        ones = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
                "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "0": ""}
        tens = {"1": "Ten", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty",
                "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety", "0": "Zero"}
        teens = {"1": "Eleven", "2": "Twelve", "3": "Thirteen", "4": "Fourteen", "5": "Fifteen",
                 "6": "Sixteen", "7": "Seventeen", "8": "Eighteen", "9": "Nineteen", "0": "Ten"}
        powers = {"1": "Thousand", "2": "Million", "3": "Billion", "0": ""}

        num_word = str(num)
        num_length = len(num_word)
        index = num_length - 1
        cur_power = 0

        str_arr = []

        while index >= 0:
            cur_arr = []
            if index - 2 >= 0 and int(num_word[index-2]) > 0:
                cur_arr.append(ones[num_word[index-2]] + " Hundred")
            if index - 1 >= 0:
                if int(num_word[index-1]) >= 2:
                    cur_arr.append(tens[num_word[index-1]])
                elif int(num_word[index-1]) == 1:
                    cur_arr.append(teens[num_word[index]])
            if index >= 0:
                if index - 1 >= 0 and int(num_word[index-1]) == 1:
                    pass
                else:
                    if int(num_word[index]) > 0:
                        cur_arr.append(ones[num_word[index]])
            if cur_arr:
                if cur_power > 0:
                    cur_arr.append(powers[str(cur_power)])
                cur_str = " ".join(cur_arr)
                str_arr.append(cur_str)
            cur_power += 1

            index -= 3
        return " ".join(str_arr[::-1])
