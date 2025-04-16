# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        
        total_cents=euros*100+cents
        self.__euros = total_cents//100
        self.__cents = total_cents%100

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"


    def __eq__(self,another):

        return (self.__euros*100+self.__cents==another.__euros*100+another.__cents)

    def __gt__(self,another):
       return (self.__euros*100+self.__cents>another.__euros*100+another.__cents)

    def  __lt__(self,another):
       return (self.__euros*100+self.__cents<another.__euros*100+another.__cents)

    def __ne__(self,another):
        return(self.__euros*100+self.__cents!=another.__euros*100+another.__cents)


    def __add__(self,another):
        
       
        total_cents=self.__euros*100+self.__cents+another.__euros*100+another.__cents
        return Money(0,total_cents)


    def __sub__(self,another):
       
        money1=self.__euros*100+self.__cents
        money2=another.__euros*100+another.__cents
        if money1<money2:
            raise ValueError(f"a negative result is not allowed")

        return Money(0,money1-money2)




if __name__=="__main__":
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)  # two euros and five cents
    # print(e1)
    # print(e2)
    # e3=Money(4,10)

    # print(e1==e3)

    # e1 = Money(4, 10)
    # e2 = Money(2, 5)

    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)
