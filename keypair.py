import rsa

class KeyPair:

    @staticmethod
    def genKeyPair(self):
        # generate keys and return an object of the KeyPair
        # remember: the private key is hashed to produce the public key
        # The public key is used to encrypt the data and the private key is used to decrypt the data
        # public key can be public (can be sent to anyone who needs to send data).
        # No one has your private key, so no one in the middle can read your data

        publicKey, privateKey = rsa.newkeys(512)

        self.__privateKey = privateKey
        self.__publicKey = publicKey
        return self

    def getPrivateKey(self):
        return self.__privateKey

    def getPublicKey(self):
        return self.__publicKey

    def printKeyPair (self):
        print("- Public Key: " +str(self.__publicKey)+ "\n- Private Key: "+str(self.__privateKey))