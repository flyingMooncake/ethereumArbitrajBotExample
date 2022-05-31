from cryptography.fernet import Fernet
import pickle

def store_encripted_private_key(privatekey):
    key = Fernet.generate_key()
    pickle.dump(key, open("decryptionkey.bin", "wb"))
    fernet = Fernet(key)
    encrypted_key = fernet.encrypt(privatekey.encode())
    pickle.dump(encrypted_key, open("encryptedPRIVATE.bin", "wb"))


def load_private_key(path_to_encrypted_private_key, path_to_decryptionkey):
    key = pickle.load(open( path_to_decryptionkey, "rb" ))
    enc_private_key = pickle.load(open( path_to_encrypted_private_key, "rb" ))
    fernet = Fernet(key)
    return fernet.decrypt(enc_private_key).decode()

if __name__ == "__main__":
   print("Imput your private Key for Encryption")
   private_key = input()
   store_encripted_private_key(private_key)
