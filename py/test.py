# import tkinter as tk
# from tkinter import messagebox

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         return False

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             return True
#         return False

# class BankApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Bank Account System")

#         # Initialize account variable
#         self.account = None

#         # UI components
#         self.create_ui()

#     def create_ui(self):
#         # Account creation section
#         tk.Label(self.root, text="Account Holder Name:").grid(row=0, column=0, padx=10, pady=5)
#         self.name_entry = tk.Entry(self.root)
#         self.name_entry.grid(row=0, column=1, padx=10, pady=5)

#         tk.Label(self.root, text="Initial Deposit:").grid(row=1, column=0, padx=10, pady=5)
#         self.deposit_entry = tk.Entry(self.root)
#         self.deposit_entry.grid(row=1, column=1, padx=10, pady=5)

#         tk.Button(self.root, text="Create Account", command=self.create_account).grid(row=2, column=0, columnspan=2, pady=10)

#         # Transaction section
#         tk.Label(self.root, text="Transaction Amount:").grid(row=3, column=0, padx=10, pady=5)
#         self.amount_entry = tk.Entry(self.root)
#         self.amount_entry.grid(row=3, column=1, padx=10, pady=5)

#         tk.Button(self.root, text="Deposit", command=self.deposit).grid(row=4, column=0, padx=10, pady=5)
#         tk.Button(self.root, text="Withdraw", command=self.withdraw).grid(row=4, column=1, padx=10, pady=5)

#         tk.Button(self.root, text="Check Balance", command=self.check_balance).grid(row=5, column=0, columnspan=2, pady=10)

#     def create_account(self):
#         name = self.name_entry.get()
#         try:
#             initial_deposit = float(self.deposit_entry.get())
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid amount for the initial deposit.")
#             return

#         if name and initial_deposit >= 0:
#             self.account = BankAccount(name, initial_deposit)
#             messagebox.showinfo("Success", f"Account created for {name} with balance ${initial_deposit:.2f}")
#         else:
#             messagebox.showerror("Error", "Invalid name or initial deposit.")

#     def deposit(self):
#         if not self.account:
#             messagebox.showerror("Error", "No account found. Please create an account first.")
#             return

#         try:
#             amount = float(self.amount_entry.get())
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid amount.")
#             return

#         if self.account.deposit(amount):
#             messagebox.showinfo("Success", f"Deposited ${amount:.2f}. Current balance: ${self.account.balance:.2f}")
#         else:
#             messagebox.showerror("Error", "Deposit amount must be greater than zero.")

#     def withdraw(self):
#         if not self.account:
#             messagebox.showerror("Error", "No account found. Please create an account first.")
#             return

#         try:
#             amount = float(self.amount_entry.get())
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid amount.")
#             return

#         if self.account.withdraw(amount):
#             messagebox.showinfo("Success", f"Withdrew ${amount:.2f}. Current balance: ${self.account.balance:.2f}")
#         else:
#             messagebox.showerror("Error", "Insufficient funds or invalid amount.")

#     def check_balance(self):
#         if not self.account:
#             messagebox.showerror("Error", "No account found. Please create an account first.")
#             return

#         messagebox.showinfo("Balance", f"Current balance: ${self.account.balance:.2f}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = BankApp(root)
#     root.mainloop()


class student:
    def __init__(self,n,a,g):
        if type(n) is str:
            self.name = n
        else:
            raise ValueError('name must be a string')
        if type(a) is int and a >= 0:
            self.age = a
        else:
            raise ValueError('age must be a non-negative integer')
        if type(g) is float and g >= 0 :
            self.grades = g
    def age(self):
        return self.__age
database = []
def create(n,a,g):
    if type(n) is str and type(a) is int and type(g) is float:
        database.append(student(n,a,g))
    else:
        raise ValueError('Invalid input')


