def test_server_health(client):
    response = client.get("/")

    assert response.status_code == 400
    assert response.json.get("status") == "ready"

