# WRITE YOUR SOLUTION HERE:
class BankAccount:

    def __init__(self,owner:str,account_no:str,bal:float):
        self.__owner=owner
        self.__account_no=account_no
        self.__bal=bal

    def deposit(self,amount:float):
        if amount>0:
            self.__bal+=amount
            self.__service_charge()

        
    
    def withdraw(self,amount:float):
        if self.__bal>amount:
            self.__bal-=amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__bal


    
    def __service_charge(self):
        self.__bal-=0.01*self.__bal


if __name__=="__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)

    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
