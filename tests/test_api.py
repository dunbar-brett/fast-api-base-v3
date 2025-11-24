def test_seeded_items(client, test_user):
    # use the user id provided by the `test_user` fixture
    resp = client.get(f"/api/items/user/{test_user}")
    assert resp.status_code == 200
    # list is returned
    result = resp.json()
    assert isinstance(result, list)
    assert len(result) >= 1


def test_create_item_and_get(client, test_user):
    payload = {"user_id": test_user, "title": "Test create", "description": "Desc"}
    r = client.post("/api/items", json=payload)
    assert r.status_code == 201
    d = r.json()
    assert d["title"] == "Test create"
    # now fetch items for user 8
    rr = client.get(f"/api/items/user/{test_user}")
    assert rr.status_code == 200
    assert any(i["title"] == "Test create" for i in rr.json())
