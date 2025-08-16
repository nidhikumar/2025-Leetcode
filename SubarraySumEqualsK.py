class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # prefix sum 0 occurs once (empty prefix)
        for x in nums:
            prefix += x
            # how many previous prefixes equal prefix - k?
            count += freq[prefix - k]
            freq[prefix] += 1
            print(count)
            print(freq)

        return count