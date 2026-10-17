from threading import Thread,Lock
from time import sleep

class Bank:
    balance=1000
    l1=Lock()
    def withdraw(self,amount):
        Bank.l1.acquire()
        if Bank.balance>=amount:
            print(f"Processing withdrawal of {amount}")
            old_balance=Bank.balance
            sleep(1)
            Bank.balance=old_balance-amount
            print(f"Withdrawal of {amount} successful")
        else:
            print(f"Insufficient balance for {amount}")
        Bank.l1.release()
b=Bank()
t1=Thread(target=b.withdraw,args=(700,))
t2=Thread(target=b.withdraw,args=(500,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Final balance:",Bank.balance)
