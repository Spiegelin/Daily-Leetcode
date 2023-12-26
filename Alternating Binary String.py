class Solution:
    def minOperations(self, s: str) -> int:
        nums = [*s]

        past = None
        count = 0
        countBack = 0
        n = len(nums)

        for i in range(n):
            current = nums[i]
            if (past == current) and (current == "0"):
                count += 1
                past = "1"
            elif (past == current) and (current == "1"):
                count += 1
                past = "0"
            else:
                past = current
        
        for i in range(n-1, -1, -1):
            current = nums[i]
            if (past == current) and (current == "0"):
                countBack += 1
                past = "1"
            elif (past == current) and (current == "1"):
                countBack += 1
                past = "0"
            else:
                past = current
            
        if (count > countBack):
            return countBack
        return count
    
    


class Solution:
    def minOperations(self, s: str) -> int:
        nums = [*s]

        pastFront = None
        pastBack = None

        countFront = 0
        countBack = 0
        n = len(nums)

        for i in range(n):
            currentFront = nums[i]
            currentBack = nums[n-i-1]

            # Check from the front
            if (pastFront == currentFront) and (currentFront == "0"):
                countFront += 1
                pastFront = "1"
            elif (pastFront == currentFront) and (currentFront == "1"):
                countFront += 1
                pastFront = "0"
            else:
                pastFront = currentFront
            
            # Check from the back
            if (pastBack == currentBack) and (currentBack == "0"):
                countBack += 1
                pastBack = "1"
            elif (pastBack == currentBack) and (currentBack == "1"):
                countBack += 1
                pastBack = "0"
            else:
                pastBack = currentBack       
            
        if (countFront > countBack):
            return countBack
        return countFront