class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        left = 0
        right = n
        for i in range(len(nums)):
            if i % 2 == 0:
                output.append(nums[left])
                left += 1
            else:
                output.append(nums[right])
                right += 1
        return output
