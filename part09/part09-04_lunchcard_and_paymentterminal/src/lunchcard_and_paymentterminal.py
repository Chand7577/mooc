# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance>=amount:
            self.balance-=amount
            return True

        return False
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment>=2.50:
            self.lunches+=1
            change=payment-2.50
            self.funds+=2.50
            return change

        return payment

    def eat_special(self, payment: float):
        if payment>=4.30:
            self.specials+=1
            change=payment-4.30
            self.funds+=4.30
            return change

        return payment
       

    def eat_lunch_lunchcard(self, card: LunchCard):

        if card.balance>=2.50:
            self.lunches+=1
            card.subtract_from_balance(2.50)
            return True
        
        return False
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
      

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance>=4.30:
            self.specials+=1
            card.subtract_from_balance(4.30)
            return True
        
        return False
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
      

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds+=amount
        card.deposit_money(amount)



if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(500)
    card.subtract_from_balance(100)
    card.subtract_from_balance(200)
    card.subtract_from_balance(200)
  