class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        num=[]
        for i in range(n):
            count=1
            for j in range(0,n):
                if i==j:
                    continue
                count=count*nums[j]
            num.append(count)
        return num


