class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        x = target
        
        # the exit condition will be if there item does not exist, so 
        while low <= high:
            mid = low + (high-low)//2
        # check midpoint for x
            if nums[mid] == x: 
                return mid
        # if x is greater in value, mid+1 is the new low.
            if x > nums[mid]:
                low = mid +1
                print(f"greater h:{high} l: {low} m: {mid}")
        # if x is lesser in value, change mid-1 to be high, low stays the same
            if x < nums[mid]:
                high = mid-1 
                print(f" less h:{high} l: {low} m: {mid}")

        return -1

        