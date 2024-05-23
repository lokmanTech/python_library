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
