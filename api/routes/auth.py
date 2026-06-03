import random
def generate_reset_token():
    # BUG: random is not cryptographically secure
    return str(random.randint(100000, 999999))
