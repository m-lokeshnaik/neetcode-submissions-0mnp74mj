class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # num=[]
        # for i in range(n):
        #     count=1
        #     for j in range(0,n):
        #         if i==j:
        #             continue
        #         count=count*nums[j]
        #     num.append(count)
        # return num
        n=len(nums)
        prefix=[1]*n
        sufix=[1]*n
        result=[1]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            sufix[i]=sufix[i+1]*nums[i+1]
        for i in range(n):
            result[i]=prefix[i]*sufix[i]
        return result


