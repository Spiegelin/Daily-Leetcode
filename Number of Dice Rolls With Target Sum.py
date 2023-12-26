class Solution:
    def __init__(self):
        self.dp = {}
        self.mod = 10**9+7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Set a Limit -> 90 is target, 30 faces -> 1*30 or 2*30, will not give us the answer
        # Faces has a number bigger than target, eliminate those posibilities
        # Range between the Minimum number for a combination and the maximum

        # MAX_FACE = min(k, target-n+1)


        # n is odd, target is even, must be #n odd even numbers
        # n is odd, target is odd, must be #n even even numbers

        # n is even, target is odd, must be #n odd odd numbers
        # n is even, target is even, must be #n even odd numbers

        MAX_NUM = n*k
        #MAX_FACE = min(k, target-n+1)
        

        key = (n,k,target)

        # Target too small or too big
        if target > MAX_NUM or target < n:
            return 0
        if target == 0:
            return 1 if n == 0 else 0
        
        #evenN = True if n % 2 == 0 else False
        #evenTarget = True if n % 2 == 0 else False

        if key not in self.dp:
            combinations = 0
            for i in range(1,k+1):
                combinations = (combinations%self.mod + self.numRollsToTarget(n-1,k,target-i)%self.mod)%self.mod

            self.dp[key] = combinations
            return combinations
        else:
            return self.dp[key]