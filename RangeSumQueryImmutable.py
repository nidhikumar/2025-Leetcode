class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for n in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + n)
        print(self.prefix_sum)


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]