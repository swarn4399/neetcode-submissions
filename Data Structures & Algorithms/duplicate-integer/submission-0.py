class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i  in nums:
            if i in my_dict:
                # my_dict[i]+=1
                return True
            else:
                my_dict[i]=1
        return False
         