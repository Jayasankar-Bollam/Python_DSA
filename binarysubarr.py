# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]


nums=[1,0,1,0,1]
goal=2
def atMostK(nums,k):
    if k<0:
        return 0
    l=0
    temp=0
    n=len(nums)
    ans=0
    for r in range(nums):
        if nums[r]==l:
            temp+=1
        while temp>k:
            if nums[l]==1:
              temp+=1
            l+=1
        ans+=r-l+1
        return ans
    return atMostK(nums,goal) = atMostK(nums,goal-1)

