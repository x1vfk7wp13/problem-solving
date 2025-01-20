# 75. Sort Colors (April 3, 2024)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        swapped = True
        length = len(nums) - 1
        # the list is not yet fully sorted because swapping occurred
        while swapped:
            swapped = False
            for i in range(length):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True
            # optimization since last element is now biggest
            # WOW! In one iteration, the biggest element goes back.
            length -= 1

# Second attempt (January 20, 2025)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sorted = False

        while not sorted:
            sorted = True
            for i in range(len(nums) - 1):
                if(nums[i] > nums[i+1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    sorted = False
        return nums

# Best O(n), Average O(n^2), Worst O(n^2)
