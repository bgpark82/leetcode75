def hasDuplicate(self, nums: List[int]) -> bool:
    # SC: O(N)
    # TC: O(N)
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
