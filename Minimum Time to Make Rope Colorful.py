class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        past = 0

        for current in range(1, len(colors)):
            if colors[past] == colors[current]:
                if neededTime[past] < neededTime[current]:
                    time += neededTime[past]
                    past = current
                else:
                    time += neededTime[current]
            else:
                past = current

        return time