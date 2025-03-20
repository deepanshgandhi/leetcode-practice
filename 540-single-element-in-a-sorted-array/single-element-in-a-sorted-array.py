class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l, h = 0, len(nums)-1
        while l<=h:
            print(l,h)
            mid = (l+h)//2
            if mid == 0:
                if nums[mid]!=nums[mid+1]:
                    return nums[mid]
                else:
                    l=mid+1
            elif mid == len(nums)-1:
                if nums[mid]!=nums[mid-1]:
                    return nums[mid]
                else:
                    h=mid-1
            else:
                if nums[mid]==nums[mid+1]:
                    if (mid-l)%2==0:
                        l=mid+2
                    else:
                        h=mid-1
                elif nums[mid]==nums[mid-1]:
                    if (h-mid)%2==0:
                        h=mid-2
                    else:
                        l=mid+1
                else:
                    return nums[mid]