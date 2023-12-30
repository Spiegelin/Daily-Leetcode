class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        d = {}
        words = "".join(words)

        for char in words:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for count in d.values():
            if (count % n != 0):
                return False
        
        return True