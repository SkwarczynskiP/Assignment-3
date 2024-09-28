# Question 1
# Give a divide-and-conquer algorithm to solve this problem:
# https://leetcode.com/problems/maximum-subarray/description/
#     Use a divide-and-conquer algorithm. Do not use Kadane's algorithm
#     Determine your algorithm's running time using the Master Theorem for recurrence relations

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def sumCrossing(arr, left, mid, right):
            leftSum, currSum = 0, 0

            for i in range(mid, left - 1, -1):
                currSum += arr[i]
                leftSum = max(leftSum, currSum)

            rightSum, currSum = 0, 0
            for i in range(mid + 1, right + 1):
                currSum += arr[i]
                rightSum = max(rightSum, currSum)

            return leftSum + rightSum

        def splitArray(arr, left, right):
            if left == right: return arr[left]

            mid = (left + right) // 2
            leftSum = splitArray(arr, left, mid)
            rightSum = splitArray(arr, mid + 1, right)
            crossingSum = sumCrossing(arr, left, mid, right)
            return max(leftSum, rightSum, crossingSum)

        return splitArray(nums, 0, len(nums) - 1)

# Running Time Using Master Theorem:
# T(n) = aT(n/b) + f(n)
# In this algorithm, the sumCrossing function contains loops that iterate over the array once for both the left
# and right halves of the array. Additionally, there are two recursive calls of the splitArray function.
# Therefore, T(n) = 2T(n/2) + O(n) where a = 2 (recursive calls), b = 2 (input size is halved)
# c = logb(a) = log2(2) = 1  =>  n^c = n^1 = n
# T(n) = O(n^c * logn) = O(nlogn)