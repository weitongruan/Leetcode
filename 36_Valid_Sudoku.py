class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        """ First Idea: Brute Force runtime: 104ms
        """
        tempset = set()
        for idx in xrange(9):
            tempset.clear()
            for jdx in xrange(9):
                if board[idx][jdx] != "." and board[idx][jdx] not in tempset:
                    tempset.add(board[idx][jdx])
                elif board[idx][jdx] != "." and board[idx][jdx] in tempset:
                    return False

        for idx in xrange(9):
            tempset.clear()
            for jdx in xrange(9):
                if board[jdx][idx] != "." and board[jdx][idx] not in tempset:
                    tempset.add(board[jdx][idx])
                elif board[jdx][idx] != "." and board[jdx][idx] in tempset:
                    return False

        for xloc in xrange(3):
            for yloc in xrange(3):
                tempset.clear()
                for idx in xrange(3):
                    for jdx in xrange(3):
                        if board[xloc*3+idx][yloc*3+jdx] != "." and board[xloc*3+idx][yloc*3+jdx] not in tempset:
                            tempset.add(board[xloc*3+idx][yloc*3+jdx])
                        elif board[xloc*3+idx][yloc*3+jdx] != "." and board[xloc*3+idx][yloc*3+jdx] in tempset:
                            return False

        return True

        """ Shorter algorithm online: 80ms
        """

        seen = [x for i, c in enumerate(board)
                    for j, c in enumerate(board[i])
                        if c != "."
                            for x in ((i, c), (c, j), (i/3, j/3, c))]
        return len(seen) == len(set(seen))