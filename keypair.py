from cryptography.hazmat.primitives.asymmetric import rsa

class KeyPair:

    @staticmethod
    def genKeyPair(self):
        # generate keys and return an object of the KeyPair
        # remember: the private key is hashed to produce the public key

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=512,
        )

        self.__privateKey = private_key
        self.publicKey = private_key.public_key()
        return self

    def printKeyPair (self):
        print("- Public Key: " +str(self.publicKey)+ "\n- Private Key: "+str(self.__privateKey))