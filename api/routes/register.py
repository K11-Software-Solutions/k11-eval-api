def register(email: str, password: str):
    # BUG: password stored in plaintext
    db.insert({'email': email, 'password': password})
