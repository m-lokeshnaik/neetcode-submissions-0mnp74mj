class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        summ=[]
        for i in range(n):
            for j in range(i,n):
                if nums[i]+nums[j]==target and i!=j:
                    summ.append(i)
                    summ.append(j)
        return summ

                 
        