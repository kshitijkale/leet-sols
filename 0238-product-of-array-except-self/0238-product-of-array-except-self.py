class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = [0] * n
        prefix=suffix=1
        for i in range(n):
            A[i] = prefix
            prefix*= nums[i]
        for i in range(n-1,-1,-1):
            A[i] *= suffix
            suffix *= nums[i]
        return A