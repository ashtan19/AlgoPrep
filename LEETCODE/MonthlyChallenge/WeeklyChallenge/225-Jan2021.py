'''
Weekly Challenge: 225
Number Q Solved: 2
Rank: 2724
'''


# 1 - 5661. Latest Time by Replacing Hidden Digits
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        s = time.split(":")

        print(s)

        h = s[0]
        m = s[1]

        if h == "??":
            h = "23"
        elif h[0] == "?":
            if int(h[1]) > 3:
                h = "1" + h[1]
            else:
                h = "2" + h[1]
        elif h[1] == "?":
            if int(h[0]) < 2:
                h = h[0] + "9"
            else:
                h = h[0] + "3"

        if m == "??":
            m = "59"
        elif m[0] == "?":
            m = "5" + m[1]
        elif m[1] == "?":
            m = m[0] + "9"

        return h + ":" + m


# 2 not working - 5662. Change Minimum Characters to Satisfy One of Three Conditions
class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        from collections import Counter

        min_change = float("inf")

        table_a, table_b = Counter(a), Counter(b)

        # Condition 3
        max_chara, max_charb = max(table_a.values()), max(table_b.values())

        min_change = min((len(a) - max_chara) +
                         (len(b) - max_charb), min_change)

        # Cond 1
        sorted_a = sorted(table_a.items(), key=lambda kv: kv[1], reverse=True)
        sorted_b = sorted(table_b.items(), key=lambda kv: kv[1], reverse=True)
        # print(sorted_a, sorted_b)

        biggestAChar, countA = sorted_a[0]
        biggestBChar, countB = sorted_b[0]

        for bChar, count in sorted_b:
            if bChar > biggestAChar:
                min_change = min(
                    min_change, (len(a) - countA + len(b) - count))
                break

        for AChar, count in sorted_b:
            if AChar > biggestBChar:
                min_change = min(
                    min_change, (len(a) - count + len(b) - countB))
                break

        biggestAChar, biggestBChar = max(table_a.keys()), max(table_b.keys())
        # print(biggestAChar, biggestBChar )

        changeA, changeB = 0, 0
        for c, count in table_b.items():
            if c <= biggestAChar:
                changeA += count

        for c, count in table_a.items():
            if c <= biggestBChar:
                changeB += count

        # print(changeA, changeB)
        min_change = min(min_change, changeA, changeB)

        return min_change


''' #2 Solution
class Solution {
    public int minCharacters(String a, String b) {
        char[] s = a.toCharArray();
        char[] t = b.toCharArray();
        int[] fa = new int[26];
        for(char c : s)fa[c-'a']++;
        int[] fb = new int[26];
        for(char c : t)fb[c-'a']++;
        
        int n = s.length + t.length;
        
        int min = 999999999;
        for(int i = 1;i <= 25;i++){
            int cost = 0;
            for(int j = i;j < 26;j++){
                cost += fa[j];
            }
            for(int j = 0;j < i;j++){
                cost += fb[j];
            }
            min = Math.min(min, cost);
        }
        for(int i = 1;i <= 25;i++){
            int cost = 0;
            for(int j = i;j < 26;j++){
                cost += fb[j];
            }
            for(int j = 0;j < i;j++){
                cost += fa[j];
            }
            min = Math.min(min, cost);
        }
        for(int i = 0;i < 26;i++){
            min = Math.min(min, n - (fa[i] + fb[i]));
        }
        return min;
    }
}
'''

# 3 Cleared - 5663. Find Kth Largest XOR Coordinate Value


class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq

        n, m = len(matrix), len(matrix[0])

        heap = []

        for i in range(n):
            for j in range(m):
                x = matrix[i][j]
                cur = x
                if i > 0:
                    cur = cur ^ matrix[i-1][j]
                if j > 0:
                    cur = cur ^ matrix[i][j-1]
                if i > 0 and j > 0:
                    cur = cur ^ matrix[i-1][j-1]

                matrix[i][j] = cur
                if len(heap) < k:
                    heapq.heappush(heap, cur)
                else:
                    heapq.heappushpop(heap, cur)
        return heap[0]
