class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mi, ni = 0, 0
        
        if not nums1 or not nums2:
            return
        
        while mi < m + n:
            if mi > m - 1:
                nums1[mi] = nums2[ni]
                ni += 1
                mi += 1
                changed = True
            else:
                if nums1[mi] <= nums2[ni]:
                    mi += 1
                else:
                    t = nums2[ni]
                    nums2[ni] = nums1[mi]
                    nums1[mi] = t
                    
        nums1.sort()
