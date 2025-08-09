class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        sumPrefix = 0
        for n in nums:
            sumPrefix += n
            self.prefix_sum.append(sumPrefix)
        print(self.prefix_sum)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left-1]