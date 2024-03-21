class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        myset = []
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                if ele != '.':
                    myset += [(i,ele), (ele,j),(i//3,j//3,ele)]
        return len(myset) == len(set(myset))
