from pathlib import Path
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''


# def load_key():
#     file = open('key.key', 'rb')
#     key = file.read()
#     file.close()
#     return key


# key = load_key()
# fer = Fernet(key)


# def view():
    
#     path = Path("passwords.txt")
    
#     contents = path.read_text()
#     lines = contents.splitlines()
#     for line in lines:
#         data = line.lstrip()
#         user, passw = data.split("|")
#         print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
                

# def add():
#     name = input("Account Name: ")
#     pwd = input("Password: ")

#     path = Path("passwords.txt")
    
#     old = path.read_text() + "\n"
#     path.write_text(old + name + "|" + fer.encrypt(pwd.encode()).decode())
    
# while True:
#     print("Password Manager")
#     print("1. Add Password")
#     print("2. View Password")
#     print("3. Exit")
#     mode = input(">>> ")

#     if mode == "1":
#         add()
#     elif mode == "2":
#         view()
#     elif mode == "3":
#         break
#     else:
#         print("Invalid input!")

def bubble_sort(arr):

    for i in range(len(arr) -1, 0, -1):

        swapped = False

        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr, size):

    for i in range(size):
        cur_min_ind = i
        for j in range(i+1, size):
            if arr[j] < arr[cur_min_ind]:
                cur_min_ind = j
        arr[i], arr[cur_min_ind] = arr[cur_min_ind], arr[i]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[i + l]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):

    if l < r:
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# arr = [12, 11, 13, 5, 6, 7]
# size = len(arr)
# # bubble_sort(arr)
# mergeSort(arr, 0, len(arr)-1)
# print(arr)

ZeroDivisionError
IndexError
ValueError
NameError
ImportError
TypeError

class BalanceException(Exception):
    pass

class BankAccount:

    def __init__(self, initial_amount, acctName):
        self.balance = initial_amount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Complete.")
        self.get_balance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acctName):
        super().__init__(initial_amount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)