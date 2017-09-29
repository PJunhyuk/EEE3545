import sys ## For force quit

class Account:
    
    ################### 1.1 #####################
    def __init__(self, *balance):
        if len(balance) == 0: ## If there is no amount input, set the balance to 0
            self.balance = 0
        elif len(balance) == 1: ## If there are 1 input value, set the balance to it
            self.balance = balance[0]
        else: ## If there are more than 1 input value, it means error, so print ERROR message, and do force quit
            print("너무 많은 값이 입력되었습니다! 잔액과 계좌번호만 입력하셔야 합니다.\n")
            sys.exit(1) ## Force quit
        self.Showinfo()

    #############################################



    ################### 1.2 #####################    
    def Account_Deposit(self, amount):
        self.balance = self.balance + amount
        self.Showinfo()

    #############################################



    ################### 1.3 #####################        
    def Account_Withdraw(self, amount):
        self.balance = self.balance - amount
        self.Showinfo()

    #############################################



    ################### 1.4 #####################     
    def Showinfo(self):
        print("잔액은 %d원 입니다.\n" % self.balance)

        
    #############################################

        


class Woori_Account(Account):



    ################### 1.5 #####################
    def __init__(self, account_number, *balance):
        self.account_number = account_number
        print("우리은행에 새로운 계좌가 생성되었습니다.")
        Account.__init__(self, *balance)

    #############################################



    ################### 1.6 #####################
    def tellAccountInfo(self):
        print("현재 우리은행 계좌는 %s입니다." % self.account_number)
        Account.Showinfo(self)

    #############################################



    ################### 1.7 #####################
    def Account_Deposit(self, amount):
        print("현재 우리은행 %s 통장에 %d원을 입금하였습니다" % (self.account_number, amount))
        Account.Account_Deposit(self, amount)

    #############################################



    ################### 1.8 #####################
    def Account_Withdraw(self, amount):
        if amount > self.balance:
            print("우리은행에 잔액이 부족합니다.")
            Account.Showinfo(self)
        else:
            print("현재 우리은행 %s 통장에 %d원을 출금하였습니다" % (self.account_number, amount))
            Account.Account_Withdraw(self, amount)

    #############################################


a = Woori_Account('111-11111')
# a = Woori_Account('111-11111', 1000)
# a = Woori_Account('111-11111', 1000, 1000)

a.tellAccountInfo()

a.Account_Deposit(1000)

a.Account_Withdraw(1000)

a.Account_Withdraw(1000)

a.tellAccountInfo()

