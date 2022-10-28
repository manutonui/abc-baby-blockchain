class Transaction:
    def __init__(self) -> None:
        self.__transactionID = None
        self.__setOfOperations = None # set of payment operations confirmed in this transaction
        self.__nonce = None # value to protect duplicate transactions with the same operations
        pass

    @staticmethod
    def createTransaction(self, setOfOperations, nonce):
        self.__setOfOperations = setOfOperations 
        self.__nonce = nonce
        return self

    def toString():
        return ""

    def printTransaction():
        pass