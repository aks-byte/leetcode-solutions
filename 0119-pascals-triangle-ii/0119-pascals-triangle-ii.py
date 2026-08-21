class Solution(object):
    def getRow(self, rowIndex):

        row =[1]

        for i in range (rowIndex):
            new_row = [1] * (len(row)+1)

            for j in range(1, len(row)):
                new_row[j] = row[j-1] + row[j]
            row = new_row
        return row
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        