from cryptography.fernet import Fernet
key = Fernet.generate_key() 
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"Hello This is XFLOW!")
print(encoded_text)
print("\n")
decoded_text = cipher_suite.decrypt(encoded_text)
print(decoded_text)
print("\n")
