"""
Leetcode: 212. Word Search II

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(M(4⋅3^(L−1) ))
Space Complexity: O(n) for the Trie

Pattern: Trie and Matrix    
Technique: Backtracking with Trie

Problems Encountered: Ran into a lot of edge case problems - bad 
Other Solutions: Can optimize by delete paths that you found - wont search for it again 

"""


class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # * denotes the Trie has this word as item
        # if * doesn't exist, Trie doesn't have this word but as a path to longer word
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()

        trie.head = {}

        for word in words:
            trie.add(word)

        trie_head = trie.head

        n = len(board)
        m = len(board[0])

        result = set()

        def search_word(trie_node, board, x, y, visited, result, path):
            top = board[x-1][y] if x-1 >= 0 else None
            bottom = board[x+1][y] if x+1 < n else None
            left = board[x][y-1] if y-1 >= 0 else None
            right = board[x][y+1] if y+1 < m else None

            if '*' in trie_node:
                result.add("".join(path))

            if top in trie_node and (x-1, y) not in visited:  # Looking top
                path.append(top)
                visited.add((x-1, y))
                search_word(trie_node[top], board, x -
                            1, y, visited, result, path)
                path.pop()
                visited.remove((x-1, y))

            if bottom in trie_node and (x+1, y) not in visited:  # Looking bottom
                path.append(bottom)
                visited.add((x+1, y))
                search_word(trie_node[bottom], board,
                            x+1, y, visited, result, path)
                path.pop()
                visited.remove((x+1, y))

            if left in trie_node and (x, y-1) not in visited:  # Looking left
                path.append(left)
                visited.add((x, y-1))
                search_word(trie_node[left], board, x,
                            y-1, visited, result, path)
                path.pop()
                visited.remove((x, y-1))

            if right in trie_node and (x, y+1) not in visited:  # Looking right
                path.append(right)
                visited.add((x, y+1))
                search_word(trie_node[right], board, x,
                            y+1, visited, result, path)
                path.pop()
                visited.remove((x, y+1))

        for i in range(n):
            for j in range(m):
                ch = board[i][j]
                if ch in trie_head:
                    search_word(trie_head[ch], board, i,
                                j, set([(i, j)]), result, [ch])

        return list(result)
