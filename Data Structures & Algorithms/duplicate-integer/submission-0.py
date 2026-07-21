class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_exists = {}
        for num in nums:
            if is_exists.get(num):
                return True
            else:
                is_exists[num]=True
        return False

        