class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         # sort array
         # pass through nums
         # for every number solve the corresponding twosum problem 
        res=[]
        nums.sort()
        for ind,i in enumerate(nums):
            if ind>0 and i==nums[ind-1]:
                continue
            p,q=ind+1,len(nums)-1
            while(p<q):
                if(nums[p]+nums[q]+i == 0):
                    res.append([i,nums[p],nums[q]])
                    p=p+1
                    while(nums[p] == nums[p-1] and p<q):
                        p=p+1
                if(nums[p]+nums[q]+i > 0):
                    q=q-1
                if(nums[p]+nums[q]+i < 0):
                    p=p+1

        return res

        