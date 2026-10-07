# src/encrypt.py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
key = AESGCM.generate_key(bit_length=256)
nonce = os.urandom(12)
ct = AESGCM(key).encrypt(nonce, b"hello", None)