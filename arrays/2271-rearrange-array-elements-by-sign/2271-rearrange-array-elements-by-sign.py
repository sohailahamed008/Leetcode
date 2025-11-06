class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        result=[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        i=0
        j=0
        while i<len(p) and j<len(n):
            result.append(p[i])
            result.append(n[j])
            i+=1
            j+=1
        return result
        
