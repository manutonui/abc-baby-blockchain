class Operation:
    def __init__(self) -> None:
        self.__sender = None
        self.__receiver = None
        self.__amount = None
        self.__signature = None

    @staticmethod
    def createOperation(self, sender, receiver, amount, signature):
        self.__sender = sender
        self.__receiver = receiver
        self.__amount = amount
        self.__signature = signature
        return self

    @staticmethod
    def verifyOperation(operation):
        # verify amount - that it does not exceed the sender's balance
        # verify signature - using sender's(account) pubKey
        return False

    def toString():
        return ""

    def printOperation():
        pass