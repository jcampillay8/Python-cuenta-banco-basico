class BankAccount:
	
	def __init__(self, int_rate=0.01, balance=0): 
		self.int_rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.amount = amount
		self.balance = self.balance + self.amount
		print("Saldo actualizado: $",self.balance)


	def withdraw(self, amount):
		self.amount=amount
		if (self.amount > self.balance):
			print("Fondos insuficientes: cobrar una tarifa de $", self.balance)
			self.balance -= self.balance
			print("Saldo actualizado: $",self.balance)
		else:
			self.balance = self.balance - self.amount
			print("Saldo actualizado: $",self.balance) 

	def display_account_info(self):
		print("Tu saldo es de: $",self.balance)
		return self.balance

	def yield_interest(self):
		self.balance = self.balance+(self.balance * self.int_rate)
		return self.balance
	

# Jaime = BankAccount()
# Jaime.deposit(200)
# Jaime.withdraw(50)
# Jaime.withdraw(200)
# Jaime.display_account_info()