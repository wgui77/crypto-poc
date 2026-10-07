# src/legacy.py
import hashlib
SECRET = "0123456789abcdef0123456789abcdef"
digest = hashlib.md5(b"data").hexdigest()