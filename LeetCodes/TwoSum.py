class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output=[]
        for i,num in enumerate(nums):
            print(target -num )
            if(target-num) in nums and nums.index(target-num)!=i:
                output.append(i)
                output.append(nums.index(target-num))
                return output
        print(output)
        
               
               
if(__name__ == 'main'):
    sol = Solution()
    sol.twoSum([1,3,5],6)