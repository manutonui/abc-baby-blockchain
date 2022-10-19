import rsa

class Signature:

    @staticmethod
    def signData (privKey, msg):
        return rsa.sign(msg.encode(), privKey, 'SHA-1')

    def verifySignature(sign, msg, pubKey):
        if rsa.verify(msg.encode(), sign, pubKey) == 'SHA-1':
            return True
        return False

    def printSignature (sign):
        print("Signature value: "+str(sign))