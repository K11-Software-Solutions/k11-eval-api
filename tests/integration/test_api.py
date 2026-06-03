def test_full_flow(client):
    r = client.post('/users', json={'email': 'a@b.com', 'password': 'pass'})
    assert r.status_code == 201
