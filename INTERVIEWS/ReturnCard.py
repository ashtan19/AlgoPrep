

input = [
    '1289,Creation,120000,2019-05-18 05:30:00',
    '1289,Load,40000,2019-05-18 05:31:00',
    '510,Creation,120000,2019-05-18 02:30:00',
    '510,Load,50000,2019-05-18 02:31:00',
    '1289,Load,10000,2019-05-18 05:31:30',
    '361,Purchase,100000,2019-05-18 06:32:00',
    '361,Load,90000,2019-05-18 06:33:00',
    '1289,Purchase,150000,2019-05-18 05:32:00',
    '1289,Load,140000,2019-05-18 05:34:00',
    '510,Purchase,150000,2019-05-18 02:32:00',
    '510,Load,100000,2019-05-18 02:34:00',
    '510,Load,10000,2019-05-18 02:33:00',
    '361,Creation,120000,2019-05-18 06:30:00',
    '361,Load,50000,2019-05-18 06:31:00',
    '7,Creation,120000,2019-05-18 09:30:00',
    '8888,Creation,50000,2019-05-18 15:30:00',
    '8888,Load,50000,2019-05-18 15:35:00',
    '10,Creation,10000,2019-05-18 14:29:00',
    '10,Load,70000,2019-05-18 14:30:00',
    '8888,Purchase,100000,2019-05-18 15:40:00',
    '8888,Load,50000,2019-05-18 15:47:00',
]

transactionTable = {}

returnsList = []

# Filtering transactions based on user card
for transaction in input:
    transactionSplit = transaction.split(",")
    userRecord = transactionTable.setdefault(
        transactionSplit[0], []).append(transactionSplit)

print(transactionTable['510'])

# Sorting Transaction of user in chronological order
for user in transactionTable.keys():
    userTransactions = transactionTable[user]
    userTransactions.sort(key=lambda userTransactions: userTransactions[3])
    transactionTable[user] = userTransactions

    hasPurchased = False
    initialLoan, curLoanValue, userLoadValue, purchaseValue, returnValue = 0, 0, 0, 0, 0

    for transaction in userTransactions:
        print(transaction)
        cardNum, action, amount, time = transaction
        amount = int(amount)

        if action == "Creation":
            initialLoan = amount
            curLoanValue = amount
        elif action == "Purchase":
            purchaseValue = amount
            hasPurchased = True
            if curLoanValue <= purchaseValue:
                purchaseValue -= curLoanValue
                curLoanValue = 0
                userLoadValue -= purchaseValue
            else:
                curLoanValue -= purchaseValue
        elif action == "Load":
            if hasPurchased == False:
                userLoadValue += amount
            else:
                returnValue += amount
                if amount >= initialLoan-curLoanValue:
                    remainder = amount - (initialLoan - curLoanValue)
                    curLoanValue = initialLoan
                    userLoadValue += remainder
                else:
                    curLoanValue += amount

    if hasPurchased == True and userLoadValue > 0:
        returnsList.append(user + "**" + str(userLoadValue))


print(transactionTable['510'])

print(returnsList)
