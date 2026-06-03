def search(q: str):
    # BUG: SQL injection vulnerability
    return db.execute(f'SELECT * FROM items WHERE name LIKE "%{q}%"')
