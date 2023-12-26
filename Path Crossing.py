class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Initial values
        start = (0,0)
        movement = [start]

        x = 0
        y = 0

        # Separate the string into a list
        directions = [*path]
        #directions = [x for x in directions]

        # Add movement
        for direction in directions:
            if (direction == "N"):
                y += 1
            elif (direction == "S"):
                y -= 1
            elif (direction == "E"):
                x += 1
            else:
                x -= 1
            
            if ((x,y) in movement):
                return True
            movement.append((x,y))
        
        return False