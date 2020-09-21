'''
Affirm Coding Challenge Questions 

You are given a stream of transaction events:
1. One is an AUTH event that pre-approves a spend amount
    1. Contains Timestamp, Card Number, AUTH, Amount
2. Another is a Capture event (Spend)
    1. Contains Timestamp, CAPTURE, Amount

Rules:
1. Capture events are associated with the AUTH card that precedes it:
    1. “[Timestamp] Card #10 AUTH 100”
    2. “[Timestamp] CAPTURE 50”
2. Negative Amounts are not valid Capture events
3. Transactions are not in order
4. Transactions between 00:00 - 07:59 and 22:00 - 23:59 are considered abnormal 

Objectives:
1. Find the Card that has the most abnormal valid transactions (negative transactions are still ignored)
    1. Return Card Number and Number of abnormal transactions
2. Find the Card that has the most invalid transactions:
    1. Return Card # and # of invalid 
3. Find the Card that has the highest spend ( highest total capture value)
    1. Return Card # and total spend


'''
