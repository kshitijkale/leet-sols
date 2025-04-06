class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] == target): 
                return mid
            if(nums[l]<=nums[mid]):     # left sorted portion
                if(target>nums[mid] or target<nums[l]):
                    l = mid + 1
                else:
                    r = mid - 1
            else:                       # right sorted
                if(target<nums[mid] or target>=nums[l]):
                    r = mid - 1 
                else:
                    l = mid + 1
        return -1