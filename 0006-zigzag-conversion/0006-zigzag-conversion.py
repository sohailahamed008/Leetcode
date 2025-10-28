class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        row=[""] * numRows
        cr=0
        di=-1
        for i in s:
            row[cr]+=i
            if cr==0 or cr==numRows-1:
                di *= -1
            cr+=di
        return "".join(row)


        