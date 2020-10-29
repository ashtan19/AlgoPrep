"""
Leetcode: Amazon OA Ways to Split String into Primes 

Attempts:1
Completed:Y
Acheived Ideal: y
Under 30 Mins: Y

Time Complexity: O(n^3)
Space Complexity: O(n)

Pattern: DP 
Technique: Use dp to track which indexes have valid combinations 

Problems Encountered:
Other Solutions:

"""


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    if n in memo_primes:
        return memo_primes[n]

    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # all other even numbers are not primes
    if not n & 1:
        memo_primes[n] = False
        return False
    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            memo_primes[n] = False
            return False
    memo_primes[n] = True
    return True


def countStringToPrime(input_string):
    dp = {-1: 1}
    n = len(input_string)

    for i in range(0, n):
        count = 0
        for prime_index in dp.keys():
            sub_string_int = int(str(input_string[prime_index+1: i+1]))
            if isprime(sub_string_int):
                count += dp[prime_index]
        if count > 0:
            dp[i] = count
    if n-1 in dp:
        return dp[n-1] % 1000000007
    else:
        return 0


memo_primes = {0: False, 1: False, 2: True, 3: True}

test_string = "11373737731"
print(countStringToPrime(test_string))
