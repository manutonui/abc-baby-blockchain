from signature import Signature

class Operation:
    def __init__(self) -> None:
        self.__sender = None
        self.__receiver = None
        self.__amount = None
        self.__signature = None

    @staticmethod
    def createOperation(self, sender, receiver, amount, signature):
        self.__sender = sender # an account
        self.__receiver = receiver # an account
        self.__amount = amount
        self.__signature = signature
        return self

    @staticmethod
    def verifyOperation(self):
        # verify amount - that it does not exceed the sender's balance
        # verify signature - using sender's(account) pubKey
        if self.__sender.getBalance() < self.__amount:
            return False
        return Signature.verifySignature(self.__signature, self.__amount, self.__sender)

    def toString():
        return ""

    def printOperation():
        pass