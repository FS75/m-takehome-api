from fastapi import status

def test_get_object(test_client):
    # Retrieve an existing object
    response = test_client.get("/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": "1",
        "full_name": "Junji Ito",
        "email": "junji.ito@abc.com",
        "mobile_number": "12345678"
    }

    # Test for non-existent object
    response = test_client.get("/4")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Object with id 4 not found"}

def test_get_all_objects(test_client):
    # Retrieve all existing objects
    response = test_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "id": "1",
            "full_name": "Junji Ito",
            "email": "junji.ito@abc.com",
            "mobile_number": "12345678"
        },
        {
            "id": "2",
            "full_name": "Kentaro Miura",
            "email": "kentaro.miura@xyz.com",
            "mobile_number": "88888888"
        },
        {
            "id": "3",
            "full_name": "Naoki Urasawa",
            "email": "naoki.urasawa@fgh.com",
            "mobile_number": "98009800"
        }
    ]

def test_create_object(test_client):
    new_object = {
        "id": "4",
        "full_name": "Osamu Tezuka",
        "email": "osamu.tezuka@ijk.com",
        "mobile_number": "77777777"
    }
    response = test_client.post("/", json=new_object)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Object added", "object": new_object}

    # Testing for object with duplicate id
    response = test_client.post("/", json=new_object)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Object with id {new_object['id']} already exists"}

def test_remove_object(test_client):
    # Testing deleting of an existing object
    response = test_client.delete("/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message": "Object with ID 1 deleted",
        "object": {
            "id": "1",
            "full_name": "Junji Ito",
            "email": "junji.ito@abc.com",
            "mobile_number": "12345678"
        }
    }

    # Testing deleting the same object again
    response = test_client.delete("/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Object not found"}
