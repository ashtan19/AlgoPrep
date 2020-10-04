"""
Leetcode: 468. Validate IP Address


Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(N)
Space Complexity: O(N)

Pattern: String Manipulation
Technique: Check all the cases that output a true

Problems Encountered: Getting all the cases right
Other Solutions: Can extract validation on IP4 and IP6 into functions as shown below

"""


class Solution:
    def validate_IPv4(self, IP):
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"

    def validate_IPv6(self, IP):
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    def validIPAddress(self, IP):
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        is_ip4, is_ip6 = True, True
        s4 = IP.split(".")
        print(s4)
        if len(s4) == 4:
            valid = False
            for x in s4:
                if len(x) > 0 and len(x) <= 4 and x.isdecimal() and int(x) < 256 and int(x) >= 0:
                    valid = True
                    if len(x) > 1 and x[0] == "0":
                        valid = False
                else:
                    valid = False
                if not valid:
                    break
            if valid:
                return "IPv4"

        s6 = IP.split(":")
        if len(s6) == 8:
            valid = False
            for x in s6:
                if len(x) > 0 and len(x) <= 4 and all(c in string.hexdigits for c in x):
                    valid = True
                else:
                    valid = False
                if not valid:
                    break

            if valid:
                return "IPv6"

        return "Neither"
