class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numFinal = [0] * (len(nums1) + len(nums2))
        numFinal = nums1 + nums2
        numFinal.sort()
        mid = len(numFinal) // 2
        
        if len(numFinal) % 2 == 0:
            return (numFinal[mid - 1] + numFinal[mid]) / 2
        else:
            return numFinal[mid]