from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii

def decrypt_aes_gcm(encryption_key: str, encrypted_value: str):
    try:
        iv_hex, encrypted_text_hex, auth_tag_hex = encrypted_value.split(":")
    except ValueError:
        print("Invalid encrypted value format. It should be IV:EncryptedText:AuthTag.")
        return
    
    key = binascii.unhexlify(encryption_key)
    
    if len(key) != 32:
        print(f"Key length is {len(key)} bytes, but it should be 32 bytes for AES-256.")
        return
    
    iv = binascii.unhexlify(iv_hex)
    encrypted_text = binascii.unhexlify(encrypted_text_hex)
    auth_tag = binascii.unhexlify(auth_tag_hex)

    if len(iv) != 12:
        print(f"IV length is {len(iv)} bytes, but it should be 12 bytes for AES-GCM.")
        return
    if len(auth_tag) != 16:
        print(f"Auth tag length is {len(auth_tag)} bytes, but it should be 16 bytes for AES-GCM.")
        return

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, auth_tag), backend=default_backend())
    decryptor = cipher.decryptor()
    
    try:
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        print("Decrypted Text:", decrypted_text.decode('utf-8'))
    except Exception as e:
        print(f"Decryption failed: {str(e)}")

def main():
    encryption_key = input("Enter the encryption key (hex-encoded string): ")
    encrypted_value = input("Enter the encrypted value (IV:EncryptedText:AuthTag): ")
    decrypt_aes_gcm(encryption_key, encrypted_value)

if __name__ == "__main__":
    main()
