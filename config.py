# Base URLs for the REST API
# POST
API_URL_OBJECT_CREATION = "https://api.restful-api.dev/objects"
# GET
API_URL_OBJECT_GET_3 = "https://api.restful-api.dev/objects?id=3"
# PUT
API_URL_OBJECT_7 = "https://api.restful-api.dev/objects/7"

# Default payloads
PAYLOAD_OBJECT_CREATION = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

PAYLOAD_OBJECT_UPDATE = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}
