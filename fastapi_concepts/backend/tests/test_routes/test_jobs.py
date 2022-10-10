import json


def test_create_job(client):
    data = {
        "title": "test-SDE-1",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }
    response = client.post("/api/v1/job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "google"
    assert response.json()["description"] == "python"


def test_fetch_job(client):  # new test
    data = {
        "title": "test-SDE-1",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }

    response = client.post("/api/v1/job/", json.dumps(data))
    response = client.get("/api/v1/job/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "test-SDE-1"


def test_fetch_jobs(client):  # new test
    data_1 = {
        "title": "test-SDE-1",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }
    data_2 = {
        "title": "test-SDE-2",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }

    response = client.post("/api/v1/job/", json.dumps(data_1))
    response = client.post("/api/v1/job/", json.dumps(data_2))
    response = client.get("/api/v1/job/")
    assert response.status_code == 200


def test_fetch_active_jobs(client):  # new test
    data_1 = {
        "title": "test-SDE-1",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": True
    }
    data_2 = {
        "title": "test-SDE-2",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": True
    }
    data_3 = {
        "title": "test-SDE-3",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }

    response = client.post("/api/v1/job/", json.dumps(data_1))
    response = client.post("/api/v1/job/", json.dumps(data_2))
    response = client.post("/api/v1/job/", json.dumps(data_3))
    response = client.get("/api/v1/job/active/")
    assert response.status_code == 200


def test_delete_job(client):
    data = {
        "title": "test-SDE-1",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }

    response = client.post("/api/v1/job/", json.dumps(data))
    response = client.delete("/api/v1/job/1")
    assert response.status_code == 200



def test_update_job(client):  # new test
    data = {
        "title": "test-SDE-1",
        "company": "google",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }
    update_data = {
        "title": "test-SDE-2",
        "company": "netflix",
        "company_url": "www.google.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "is_active": False
    }

    response = client.post("/api/v1/job/", json.dumps(data))
    response = client.put("/api/v1/job/1", json.dumps(update_data))
    assert response.status_code == 200
    # assert response.json()['company'] == "netflix"