class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        a = [0] * length
        for i in range(length):
            a[(i+k) % length] = nums[i]
        nums[:] = a
        return nums


a = Solution()
print(a.rotate([1, 2, 3, 4, 5, 6, 7], 3))
