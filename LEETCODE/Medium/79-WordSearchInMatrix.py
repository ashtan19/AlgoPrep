"""
Leetcode:79. Word Search

Attempts: 1
Completed: Y
Acheived Ideal: N

Time Complexity: O(n * len(word))
Space Complexity: O(word)

Pattern: Linear Search in Matrix 
Technique: Checking if char are adjacent to previous char

Problems Encountered: Took a long time to write out logic 
Other Solutions:

"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == [[]] or board == [] or board == None:
            return False

        isSeen = {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (
                    board[row][col] == word[0]
                    and searchWord(board, row, col, word, 0, isSeen) == True
                ):
                    return True

        return False


def searchWord(board, row, col, word, currentindex, isSeen):
    if currentindex == len(word) - 1:
        return True
    isSeen[(row, col)] = True
    currentchar = word[currentindex + 1]
    if row - 1 >= 0:
        if (
            isSeen.get((row - 1, col)) == None
            and board[row - 1][col] == currentchar
            and searchWord(board, row - 1, col, word, currentindex + 1, isSeen)
        ):
            return True

    if row + 1 < len(board):
        if (
            isSeen.get((row + 1, col)) == None
            and board[row + 1][col] == currentchar
            and searchWord(board, row + 1, col, word, currentindex + 1, isSeen)
        ):
            return True

    if col - 1 >= 0:
        if (
            isSeen.get((row, col - 1)) == None
            and board[row][col - 1] == currentchar
            and searchWord(board, row, col - 1, word, currentindex + 1, isSeen)
        ):
            return True
    if col + 1 < len(board[0]):
        if (
            isSeen.get((row, col + 1)) == None
            and board[row][col + 1] == currentchar
            and searchWord(board, row, col + 1, word, currentindex + 1, isSeen)
        ):
            return True

    del isSeen[(row, col)]

    return False

