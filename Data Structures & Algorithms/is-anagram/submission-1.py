

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        s_list = list(s)

        if len(t_list) != len(s_list):
            return False

        for letter in s_list:
            if letter in t_list:
                t_list.remove(letter)
            else:
                return False
        return True 
        

sol = Solution()

class Test:
    def same_word_not_anagram(self):
        s ='asdfasd'
        t ='asdfasd'
        assert sol.isAnagram(s,t) == True
    def diff_length(self):
        print("diff len")
        assert sol.isAnagram("afaf","afa") == False


test=Test()
test.same_word_not_anagram()
test.diff_length()

        