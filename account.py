from keypair import KeyPair
from signature import Signature as Sign

class Account:

    def __init__(self):
        # when creating a new account: generate first keypair to generate account id
        self.__accountID = None # can be pubKey or its hash
        self.__wallet = [] # list of keypairs
        self.__balance = 0

    @staticmethod
    def genAccount(self):
        # create a new account, generate a key pair and assign to the account
        keypair = KeyPair.genKeyPair(KeyPair())
        self.addKeypairToWallet(keypair)

        # if accountID is empty, assign
        if not self.__accountID:
            self.assignAccountID(keypair.getPublicKey())
            
        return self

    def addKeypairToWallet(self, keypair):
        # append keyPair to wallet
        self.__wallet.append(keypair)

    def updateBalance(self, balance):
        self.__balance = balance

    def getBalance(self) -> int:
        return self.__balance

    def printBalance(self):
        print(self.__balance)

    def signData(self, msg, index) -> bytes:
        privateKey = self.__wallet[index]
        return Sign.signData(privateKey, msg)

    def createOperatoin(recipient, amount, index): # returns object of operation class
        # recipient is an account object
        # amount to transact
        # index of key in the wallet

        return None

    def toString():
        pass

    def printAcc(self):
        print("AccountID: "+str(self.__accountID)+"\nKeyPairs: "+str(self.__wallet))

    def assignAccountID(self, pubKey): # hash pubKey and assign to accountID
        hashVal = int(hash(pubKey))
        hashOfPub = hashVal if hashVal > 0 else hashVal*-1 # to avoid negative values
        self.__accountID = hashOfPub

