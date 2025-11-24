def test_seeded_items(client):
    # assume seed_db.py was run or tests run after create_tables + seed
    resp = client.get("/api/items/user/8")
    assert resp.status_code == 200
    # list is returned
    assert isinstance(resp.json(), list)


def test_create_item_and_get(client):
    payload = {"user_id": 8, "title": "Test create", "description": "Desc"}
    r = client.post("/api/items", json=payload)
    assert r.status_code == 201
    d = r.json()
    assert d["title"] == "Test create"
    # now fetch items for user 8
    rr = client.get("/api/items/user/8")
    assert rr.status_code == 200
    assert any(i["title"] == "Test create" for i in rr.json())
