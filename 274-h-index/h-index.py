class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r = 0,5000
        n= len(citations)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            count = 0
            for c in citations:
                if c >= mid:
                    count+=1
            print(mid,count)
            if count >= mid:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans