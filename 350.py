from collections import defaultdict


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        both = list(set(nums1) & set(nums2))
        result = []
        for item in both:
            count = min(nums1.count(item), nums2.count(item))
            result.extend([item] * count)
        return result

        d1, d2 = defaultdict(int), defaultdict(int)
        for item in nums1:
            d1[item] += 1
        for item in nums2:
            d2[item] += 1

        result = []
        for k,count in d1.items():
            if k in d2:
                result.extend([k] * min(count, d2[k]))
        return result

