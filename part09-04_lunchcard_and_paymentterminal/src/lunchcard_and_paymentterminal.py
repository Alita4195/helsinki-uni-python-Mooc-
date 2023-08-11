# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance+=amount


    def subtract_from_balance(self, amount: float):
        
        if amount <= self.balance:
            self.balance -= amount
            return "True"
        else:
            return "False"

        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment>= 2.50:
            payment-=2.50
            self.lunches+=1
            self.funds +=2.5
            return payment
        else:
            return payment

        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
    
    def eat_special(self, payment: float):
        if payment>= 4.30:
            payment-=4.30
            self.specials+=1
            self.funds += 4.30
            return payment
        else:
            return payment
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.


    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >=2.50:
            card.balance-=2.50
            self.lunches+=1
            return "True"
        else:
            return "False"

        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance >=4.30:
            card.balance-=4.30
            self.specials+=1
            return "True"
        else:
            return "False"
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
    

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance+=amount
        self.funds+=amount
        return card.balance


if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)