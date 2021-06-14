class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = len(nums)/2
        nums.sort()
        cTimes = 1
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                cTimes += 1
                if cTimes > times:
                    return nums[i]
            else:
                cTimes = 1
                
        return nums[0]
