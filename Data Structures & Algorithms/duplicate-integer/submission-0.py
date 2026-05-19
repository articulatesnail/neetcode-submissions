
    

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for i in nums:
            if i in l:
                return True
            else:
                l.append(i)
        return False
        
         
class Test:
    def test_no_duplicate(self):
        s = Solution()
        assert s.hasDuplicate([1,2,3]) == False

    def test_duplicate(self):
        s = Solution()
        assert s.hasDuplicate([1,2,3,3]) == True

t = Test()
t.test_no_duplicate()
t.test_duplicate()