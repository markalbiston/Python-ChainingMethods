class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
        # print('hello')

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
mark = User("Mark Albiston", "mark@me.com")

guido.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()
monty.make_deposit(300).make_deposit(300).make_withdrawal(100).make_withdrawal(100).display_user_balance()
mark.make_deposit(1000).make_withdrawal(300).make_withdrawal(300).make_withdrawal(300).display_user_balance()
print("------------BONUS TRANSFER TO MAKE ME RICH--------------")
guido.transfer_money(mark, 500).display_user_balance()
monty.display_user_balance()
mark.display_user_balance()
