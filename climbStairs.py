import pdb

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    if n == 1 or n == 2:
        return n
    
    memo = {1:1, 2:2}
    
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(climbStairs(1))
print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(6))
print(climbStairs(7))
print(climbStairs(8))
print(climbStairs(9))
print(climbStairs(10))