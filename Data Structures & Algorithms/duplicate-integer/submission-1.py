class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup  = {}
        for num in nums:
            if num in dup:
                dup[num] += 1
            else:
                dup[num] = 1

        for k, v in dup.items():
            if v > 1:
                return True
        return False

        