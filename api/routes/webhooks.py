import hmac, hashlib
def verify_signature(payload: bytes, sig: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f'sha256={expected}', sig)
