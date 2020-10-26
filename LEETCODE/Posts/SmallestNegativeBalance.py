"""
Leetcode: Smallest Negative Balance

Attempts:
Completed:
Acheived Ideal:
Under 30 Mins: 

Time Complexity:
Space Complexity:

Pattern: 
Technique: 

Problems Encountered:
Other Solutions:

"""


group = [["Alex", "Blake", 2],
         ["Blake", "Alex", 2],
         ["Casey", "Alex", 5],
         ["Blake", "Casey", 7],
         ["Alex", "Blake", 4],
         ["Alex", "Casey", 4]]

group_dict = {}

for member in group:
    borrower = member[0]
    lender = member[1]
    amount = member[2]

    if borrower in group_dict:
        group_dict[borrower] -= amount
    else:
        group_dict[borrower] = -1 * amount

    if lender in group_dict:
        group_dict[lender] += amount
    else:
        group_dict[lender] = amount

value_sorted = sorted(group_dict.values())
min_value = value_sorted[0]

result = []
for key in group_dict.keys():
    if group_dict[key] == min_value:
        result.append(key)

print(result)
