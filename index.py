from keypair import KeyPair
from signature import Signature

keyPair = KeyPair.genKeyPair(KeyPair())
# keyPair.printKeyPair()

privateKey = keyPair.getPrivateKey()

publicKey = keyPair.getPublicKey()

msg = "Whoever believes in Him shall not perish"

signature = Signature.signData(privateKey, msg)

# Signature.printSignature(signature)

verifySignature = Signature.verifySignature(signature, msg, publicKey)

# print(verifySignature)

