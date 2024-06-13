from cbtransaction import *

class Account:
    minDeposit=100000
    
    #default pin 123456
    def __init__(self, noac, nama, nik):
        self.noac=noac
        self.nama=nama.upper()
        self.nik=nik
        self.pin="123456"        
        self.balance=0
        self.transaction = LinkedListTransaction()

    #tambahkan pemeriksaan amount > 0
    def deposit(self, cabang, amount):    
        self.balance+=amount
        self.transaction.newTransaction(cabang, "12", amount)
        
    #tambahkan pemeriksaan amount > 0
    #tambahkan pemeriksaan setelah penarikan tidak boleh < dari minDeposit
    def withdraw(self, cabang, amount):
        self.balance-=amount
        self.transaction.newTransaction(cabang, "21", amount)

    def show(self):
        print("\n\n>>RINCIAN ACCOUNT\n\n")
        print("No.AC:", self.noac)
        print("Nama:", self.nama)
        print("NIK:", self.nik)
        print("Amount:", f'{self.balance:,}')

    def print(self):
        print(self.noac.ljust(14), self.nama.ljust(50), self.nik.ljust(16))

class AccountNode:
    def __init__(self, account):
        self.account=account
        self.next = None

class LinkedListAccount:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
        
    def newAccount(self,cabang, nik, nama):
        self.count+=1
        noac=cabang + str(self.count).rjust(4,"0")
        account=Account(noac, nama, nik)
        newNode = AccountNode(account)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return account
            
    def find(self, noac):
        lastPosition = self.head
        while lastPosition:
            if lastPosition.account.noac==noac:
                return lastPosition.account
            lastPosition=lastPosition.next
        return None
        
    def list(self):
        lastPosition=self.head
        print("\n\n>>DAFTAR ACCOUNT\n\n")
        print("-"*(80+3))
        print("No.AC".ljust(14),"Nama".ljust(50),"NIK".ljust(16))
        print("-"*(80+3))
        while lastPosition:
            lastPosition.account.print()
            lastPosition=lastPosition.next

#unit test
#12=Sumatera Utara, 71=Kota Medan, 11=Medan Johor, 01=Cabang 01, 01=Tabungan
#cabang="1271110101"
#savingAccount=LinkedListAccount()
#account1=savingAccount.newAccount(cabang, "1271181906730004", "Hendra Soewarno")
#assert account1.nik=="1271181906730004", "Error NIK 1271181906730004"
#account2=savingAccount.newAccount(cabang, "1271181906730005", "Susan")
#account3=savingAccount.newAccount(cabang, "1271181906730006", "Felicia Fortuna")
#account4=savingAccount.newAccount(cabang, "1271181906730007", "Viona Victoria")
#savingAccount.list()
#myAccount = savingAccount.find(account1.noac)
#myAccount.show()
#myAccount.deposit(cabang, 100000)
#assert myAccount.balance==100000, "Error Deposit, new balance 100000 not match"
#myAccount.show()
#myAccount.deposit(cabang, 100000)
#assert myAccount.balance==100000, "Error Deposit, new balance 200000 not match"
#myAccount.show()
#myAccount.withdraw(cabang, 100000)
#assert myAccount.balance==100000, "Error Deposit, new balance 100000 not match"
#myAccount.show()
#myAccount.transaction.list()