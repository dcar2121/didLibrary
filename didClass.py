import json
import hashlib
from ecdsa import SigningKey, SECP256k1
from bit import Key

class DIDLibrary:
    def __init__(self):
        self.keys = {}
        self.did = None

    def generate_key_pair(self, method="ecdsa"):
        if method == "ecdsa":
            sk = SigningKey.generate(curve=SECP256k1)
            vk = sk.get_verifying_key()
            self.keys["private"] = sk.to_string().hex()
            self.keys["public"] = vk.to_string().hex()
        elif method == "ed25519":
            sk = SigningKey.generate()
            self.keys["private"] = sk.to_string().hex()
            self.keys["public"] = sk.get_verifying_key().to_string().hex()
        return self.keys

    def register_did(self, did_method, public_key, private_key):
        if public_key != self.keys.get("public") or private_key != self.keys.get("private"):
            raise ValueError("Public and private keys do not match.")
        
        self.keys["public"] = public_key
        self.keys["private"] = private_key
        self.did = f"{did_method}:{hashlib.sha256(public_key.encode()).hexdigest()}"
        return self.keys

    def get_did(self):
        return self.did if self.did else "DID not generated."

# Example usage:
library = DIDLibrary()
key_pair = library.generate_key_pair()
print(key_pair)

# Optionally register a DID using the register_did method
library.register_did("did:sov", key_pair["public"], key_pair["private"])
print(library.keys)

# And get the DID using the get_did method
did = library.get_did()
print(did)
