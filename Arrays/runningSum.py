class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        output = []
        for i in range(len(nums)):
            sum += nums[i]
            output.append(sum)
        return output
