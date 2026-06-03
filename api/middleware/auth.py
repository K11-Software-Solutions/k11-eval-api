import jwt
SECRET = 'hardcoded-secret'   # BUG: should be from env
def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=['HS256'])
