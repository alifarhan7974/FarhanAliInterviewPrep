class Solution: 
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums) 


test = Solution()

assert test.hasDuplicate([]) == False

assert test.hasDuplicate([1]) == False

assert test.hasDuplicate([1, 2, 3, 4]) == False

assert test.hasDuplicate([1, 1, 2, 2]) == True

assert test.hasDuplicate([1, 2, 3, 4, 5, 6, 6]) == True