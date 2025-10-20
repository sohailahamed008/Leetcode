class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        m=0
        for i in range(len(accounts)):
            for j in range(len(accounts[0])):
                s+=accounts[i][j]
            if s>m:
                m=s
            s=0
        return m
            

        