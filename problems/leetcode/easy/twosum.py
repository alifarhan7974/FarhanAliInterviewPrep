class Solution:
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
    
    def twoSum(self, nums: list[int], target: int) -> list[int]: #more effieicient
        # target = nums[i] + nums[j], diff = nums[j] = target - nums[i]
        differences_map = {}
        for i in range(0, len(nums)):
            if nums[i] in differences_map:
                return [differences_map[nums[i]], i]
            
            difference = target - nums[i] #current number difference
            differences_map[difference] = i

            
                

    
                
test = Solution()

assert test.twoSum([3, 4, 5, 6], 7) == [0, 1], test.twoSum([3, 4, 5, 6], 7)

assert test.twoSum([4, 5, 6], 10) == [0, 2], test.twoSum([4, 5, 6], 10) 

assert test.twoSum([5, 5], 10) == [0, 1] 

