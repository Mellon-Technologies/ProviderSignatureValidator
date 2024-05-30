import datetime
from binascii import hexlify, unhexlify

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature




def generate_signature(clear_text):
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    digest = hashes.Hash(hashes.SHA256())
    digest.update(clear_text.encode())
    hashed_text = digest.finalize()

    # Sign the data
    signature = private_key.sign(
        clear_text.encode(),
        ec.ECDSA(hashes.SHA256())
    )

    hex_signature = hexlify(signature).decode().upper()
    return hex_signature



def verify_signature(clear_text, signature):
    with open("public_key.pem", "r") as key_file:
        key_data = key_file.read()
        if not "BEGIN PUBLIC KEY" in key_data:
            key_data = f'-----BEGIN PUBLIC KEY-----\n{key_data}\n-----END PUBLIC KEY-----'
        
        public_key = serialization.load_pem_public_key(key_data.encode())


    try:
        int(signature, 16)
    except ValueError:
        raise ValueError('Signature is not hexadecimal')
    
    clear_values = clear_text.split(';')
    if len(clear_values) != 8:
        raise ValueError('Clear text string does not contain 8 values')
    
    try:
        datetime.datetime.strptime(clear_values[2], '%Y%m%d%H%M%S')
    except:
        raise ValueError('Invalid date/time')
    
    if len(clear_values[7]) != 8:
        raise ValueError('Terminal ID is not 8 characters')
    
    for value in clear_values[3:7]:
        try:
            int(value)
        except:
            raise ValueError(f'Cleartext value {value} is not integer')


    decoded_signature = unhexlify(signature)

    try:
        public_key.verify(decoded_signature, clear_text.encode(), ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False
