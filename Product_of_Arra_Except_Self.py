#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = []
        nums = tuple(nums)
        
        for i in range(len(nums)):
            product_list = list(nums)
            product_list.pop(i)
            product=1
            for num in product_list:
                product*=num
            answer.append(product)
        return answer
            
                
            
            
