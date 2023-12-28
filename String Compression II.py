 # O(n*k*prev_len) -> O(n^2*k)
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Save memory using a hashmap avoiding repeating steps
        cache = {}

        def length(i, k, prev, prev_len):
            if (i, k, prev, prev_len) in cache:
                return cache[(i, k, prev, prev_len)]
            # We don't need to delete anything, so return something so big that it doesn't considers it
            if k < 0:
                return float("inf")

            # If out of bounds
            if i == len(s):
                return 0
            
            if s[i] == prev:
                # Only keep track of length when 1->2, 9->10, 99->100
                if prev_len in [1, 9, 99]:
                    increment = 1
                else:
                    increment = 0
                count = increment + length(i+1, k, prev, prev_len + 1)
            else:
                # Minimum between delete s[i] or Not delete
                count = min(length(i+1, k-1, prev, prev_len), 1 + length(i+1, k, s[i], 1))
            
            # Add new len to the hashmap
            cache[(i, k, prev, prev_len)] = count
            return count
                
        return length(0, k, "", 0)