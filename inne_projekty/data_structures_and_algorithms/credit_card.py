# Developed for use with the book:
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._count = 0
        self._amount = 0  # initial value for monthly payments
    
    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit: #if charge would exceed limit,
            return False                   # cannot accept charge
        else:
            self._balance += price
            self._count += 1
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._amount += amount
        self._balance -= amount
        
    def process_month(self):
        pass
    
    
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr, amount=0):
        """Create a new predatory credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self._balance += 5 # assess penalty
        if self._count > 10:
            self._balance += 1 #additional surcharge for more than 10 charges                     in month         
        return success         # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
        if self._amount < self._balance * 0.1:
            self._balance += 15  # a fee for not making minimum payment
            print("The bank added to your account's balance a fee for not paying minimal month payment of your credit")


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Les Tlaka', 'Misssipi_Regional',
                            '4455 0022 0000 3333', 2500))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings',
                            '5391 0375 9387 5309', 2500, 0.0825))
    wallet.append(CreditCard('John Bowman', 'California Federal',
                            '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance',
                            '5391 0375 9387 5309', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val)
        wallet[2].charge(2 * val)
        wallet[3].charge(3 * val)
        
    #for i in range(20):
     #   wallet[1].charge(10)

    for c in range(4):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].process_month()
            wallet[c].make_payment(100)
        print('New balance =', round(wallet[c].get_balance(), 2))
        print()
