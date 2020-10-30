"""
Leetcode: Amazon OA Throttling Gateway 
Link: https://leetcode.com/discuss/interview-question/895851/

Attempts: 1
Completed: N but have a conceptual idea of how to do it
Acheived Ideal:
Under 30 Mins: 

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: 
Technique: Track the num of requests in 10second window and 60 second window
            Take the number of requests for that second, check if contraints for 1s, 10s, and 60s
            Keep subtracting the number of available request spots and add the result num to both windows
                alternatively, you can find (maxlimit - windows) for all windows and take the min and add to all 
                assuming that you have already subtracted the left side of the window
            Add the dropped reqs
            

Problems Encountered:
Other Solutions:

"""
