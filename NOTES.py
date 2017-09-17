1. Two Sum
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

http://blog.csdn.net/github_37214932/article/details/53954430
解答方法一：双重循环尝试， 复杂度O(n^2)
解法非常直观， 但是复杂度O(n^2)，所以效率很差，在leetcode上无法通过： Submission Result: Time Limit Exceeded
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
            
        """
        
        list1=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target==nums[i]+nums[j]  and i<j: 
                    list1.append(i)
                    list1.append(j)
        return list1
        
解答方法二：用hash表储存每个数的下标，增加空间使用来加速查找至O(n)

分析： 之前O(n^2)的原因是我们做了太多次无谓的运算。事实上，既然我们知道了和与一个参数，只要判断下他们的差（和 - 参数一）存不存在即可。

而用哈希表的话，这个判断存不存在只有O(1)。