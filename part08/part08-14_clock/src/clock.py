# Write your solution here:
class Clock:
    def __init__(self,hours,mins,secs):
        self.hours=hours
        self.mins=mins
        self.secs=secs

    def __str__(self):
        return f"{self.hours:02d}:{self.mins:02d}:{self.secs:02d}"


    def set(self,hours,mins):
        self.hours=hours
        self.mins=mins
        self.secs=0


    def tick(self):
        self.secs+=1
        if self.secs==60:
            self.mins+=1
            self.secs=0

        if self.mins==60:
            self.hours=0
            self.mins=0
            self.secs=0

if __name__=="__main__":
    clock = Clock(10, 10, 58)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
   
