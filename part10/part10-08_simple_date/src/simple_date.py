# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year


    def __eq__(self,another):
        return f'{self.day}.{self.month}.{self.year}'==f"{another.day}.{another.month}.{another.year}"

    
    def __gt__(self,another):
        if self.year!=another.year:
            return self.year>another.year

        elif self.month!=another.month:
            return self.month>another.month
        
        else:
            return self.day>another.day

    
    def __ne__(self,another):
        return not self.__eq__(another)

    
    def __le__(self,another):
        lessthan=self<another
        return lessthan


    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


    def __add__(self,another):
        day=self.day+another
        month=self.month
        year=self.year

        while day>30:
            day=day-30
            month+=1

            if month>12:
                month=1
                year+=1


        return SimpleDate(day,month,year)


    def __sub__(self,another):
        self_days = self.year * 360 + (self.month - 1) * 30 + self.day
        another_days = another.year * 360 + (another.month - 1) * 30 + another.day
        return abs(self_days - another_days)



if __name__=="__main__":

    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = SimpleDate(28, 12, 1985)
    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    # d3 = d1 + 3
    # d4 = d2 + 400
    # print(d3)
    # print(d4)
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)

