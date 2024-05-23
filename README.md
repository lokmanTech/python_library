# <a id='top'>LeetCode</a> 
LeetCode problem solutions via **python3** with detailed explanations and optimized algorithms for efficient problem-solving.

|Table of Contents|
|:---------------:|
|[Add Two Integers](#2235)|
|[Running Sum of 1d Array](#1480)|
|[Richest Customer Wealth](#1672)|

### <a id='2235'>2235. Add Two Integers</a>
------------[Back to the TOP ↑](#top)--------------

Given two integers `num1` and `num2`, return the sum of the two integers.

Example 1:

- `Input: num1 = 12, num2 = 5`
- `Output: 17`
- `Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.`

Example 2: 

- `Input: num1 = -10, num2 = 4`
- `Output: -6`
- `Explanation: num1 + num2 = -6, so -6 is returned.`

Constraints:

-100 <= num1, num2 <= 100

```python3
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
    
# Example 1
solution = Solution()
num1 = 12
num2 = 5
print(solution.sum(num1, num2)) #Output: 17

# Example 2
num1 = -10
num2 = 4
print(solution.sum(num1, num2)) #Output: -6
```        


Run the solution [add_two_integers.py](python3/add_two_Integers.py)

### <a id='1480'>1480. Running Sum of 1d Array</a>
------------[Back to the TOP ↑](#top)--------------

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

- `Input: nums = [1,2,3,4]`
- `Output: [1,3,6,10]`
- `Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].`

Example 2:

- `Input: nums = [1,1,1,1,1]`
- `Output: [1,2,3,4,5]`
- `Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].`

Example 3:

- `Input: nums = [3,1,2,10,1]`
- `Output: [3,4,6,16,17]`
 

Constraints:

1 <= nums.length <= 1000

-10^6 <= nums[i] <= 10^6

```python3
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_array = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            running_sum_array.append(current_sum)
            
        return running_sum_array
        
# Example usage:
solution =  Solution()
nums1 = [1, 2, 3, 4]
print(solution.runningSum(nums1)) #Output: [1, 3, 6, 10]

nums2 = [1, 1, 1, 1, 1]
print(solution.runningSum(nums2)) #Output: [1, 1, 1, 1, 1]

nums3 = [3, 1, 2, 10, 1]
print(solution.runningSum(nums3)) #Output: [3, 1, 2, 10, 1]
```

Run the solution [Running Sum of 1d Array.py](python3/running_sum_of_1d_array.py)

### <a id='1672'>1672. Richest Customer Wealth</a>
------------[Back to the TOP ↑](#top)--------------

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100

```python3
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0 # Initialize the maximum wealth to zero
        
        for customer_accounts in accounts:
            current_wealth = sum(customer_accounts) # Calculate the wealth of the current customer
            if current_wealth > max_wealth:
                max_wealth = current_wealth # Update max_wealth if current_wealth is greater
                
        return max_wealth # Return the maximum wealth found
    
# Example usage
solution = Solution()

accounts1 = [[1,2,3],[3,2,1]]
print(solution.maximumWealth(accounts1)) # Output 6

accounts2 = [[1,5],[7,3],[3,5]]
print(solution.maximumWealth(accounts2)) # Output 10

accounts3 = [[2,8,7],[7,1,3],[1,9,5]]
print(solution.maximumWealth(accounts3)) # Output 17
```
Run the solution [Richest Customer Wealth.py](python3/richest_customer_wealth.py)
