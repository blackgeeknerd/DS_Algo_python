class CreditCard:
    """A Consumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit, initialdeposit=0):
        """Creates a new credit card instance 
        
        The Intial balance is zero
        
        customer -> the name of the customer(e.g, 'John Doe')
        bank -> the name of the bank (e.g., 'First Bank Of Nigeria')
        acnt -> The account identifier(e.g., '5391 0375 82')
        limit -> credit limit(measured in naira)
        
        """
        
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
        self._nonzero = 1000
        
        if self._nonzero > 0:
            self._balance += initialdeposit
        
    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank name"""
        return self._bank
    
    def get_account(self):
        """Returns the account number"""
        return self._acnt
    
    def get_balance(self):
        """Returns the current balance of the card."""
        return self._balance
    
    def get_limit(self):
        """Return current credit limit"""
        return self._limit
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else: 
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        if amount > 0:
            self._balance -= amount
        else:
            print(ValueError("Kindly input a number greater than 0"))
        
        
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    
    OVERLIMIT_FEE = 5 #IN naira
    
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        
        The Intial balance is zero
        
        customer    the name of the customer (e.g 'Seyi Majekobaje')
        bank        the name of the bank (e.g, 'First Bank of Nigeria')
        acnt        the account identifier (e.g '5467 3981 23')               
        limit       credit limit (measured in naira)
        apr         annual percentage rate (e.g, 0.0825 for 8.25% APR)
        """
        
        super().__init__(customer, bank, acnt, limit) #call to super class constructor
        self._apr = apr
        
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge is processed.
        Return False and assess #5 fee if charge is denied.
        """         
        
        success = super().charge(price)     #call inherited method
        if not success:     
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE           #assess penalty
        return success                      #caller expects return value
    
    
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        
        if self._balance>0:
            #if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor    

if __name__ == '__main__':
    
    wallet = []
    wallet.append(CreditCard('Seyi Majek','First Bank of Nigeria', '1234567891',10000))
    wallet.append(CreditCard('Wunmi Majek','Wema Bank', '5460982345',10000))
    wallet.append(CreditCard('Gbemi Odelade','Polaris Bank', '8745102834',10000))
    
    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(len(wallet)):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =',wallet[c].get_balance())
        print()
        
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(10)
            print('New Balance =', wallet[c].get_balance())
            print()       
        
    
    apexCard = CreditCard('Seyi Me', 'GTB', 5823456787,10000, 50)
    print(apexCard.get_balance())
         



    
    