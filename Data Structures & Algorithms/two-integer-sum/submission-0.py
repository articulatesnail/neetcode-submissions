class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}

        for k, val in enumerate(nums):
            diff = target - val
            if diff in preMap:
                return [preMap[diff],k]
            else:
                preMap[val] = k


        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-1):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

s=Solution()
class Test:
    def find_first_2_sums(self):
        assert s.twoSum([1,2,4], 6) == [1,2]

t = Test()
t.find_first_2_sums()

