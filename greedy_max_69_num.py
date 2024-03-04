"""
You are given a positive integer num consisting only 
of digits 6 and 9.

Return the maximum number you can get by changing at 
most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 
Constraints:
    1 <= num <= 104
    num consists of only 6 and 9 digits.
"""
import math

class Solution:
    def maximum69Number(self, num: int) -> int:
        
        stack = []
        change_num = False
        ans = 0

        while num > 1:
            remainder = int(num % 10)
            num = int(num / 10)
            stack.append(remainder)
            # print(f"{num} - {remainder}")

        while len(stack) > 0:
            digit = stack.pop()
            if change_num == False:
                if digit == 6:
                    digit = 9
                    change_num = True
            ans += digit * (10 ** len(stack))

        return ans

    def maximum69Number2(self, num: int) -> int:

        def helper(num: int) -> int:
            if num < 10:
                return 9

            base_10 = 10 ** int(math.log10(num))    # 1000
            number = int(num/base_10)               # 9
            number_base_10 = base_10 * number       # 9000
            remainder = num - number_base_10        #  696  

            if number == 9:
                return number_base_10 + helper(remainder)

            return number_base_10 + 3 * base_10 + remainder

        return helper(num)


sol = Solution()

num = 9669
print(sol.maximum69Number2(num))

num = 9996
print(sol.maximum69Number2(num))

num = 9999
print(sol.maximum69Number2(num))
