class Solution:
    def dayOfYear(self, date: str) -> int:
        month = int(date[5:7])
        days = int(date[8:])
        year = int(date[:4])
        isLeap = False

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    isLeap = True
                else:
                    isLeap = False
            else:
                isLeap = True
        else:
            isLeap = False

        for i in range(1,month):
            if isLeap and i == 2:
                days += 29
            elif i == 2:
                days += 28
            elif i in [4,6,9,11]:
                days += 30
            else:
                days += 31
            
        return days