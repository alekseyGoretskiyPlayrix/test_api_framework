# Base URLs for the REST API
API_BASE_URL = "https://api.restful-api.dev/objects"
# POST
API_URL_OBJECT_CREATION = "https://api.restful-api.dev/objects"
# GET
API_URL_OBJECT_GET = "https://api.restful-api.dev/objects/"
# PUT
API_URL_OBJECT_PUT = "https://api.restful-api.dev/objects/"
# DELETE
API_URL_OBJECT_DELETE_WITHOUT_ID = "https://api.restful-api.dev/objects/"

#Status codes
STATUS_CODE_200 = 200

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

PAYLOAD_GET_OBJECT_3 = {
    "id": "3",
    "name": "Apple iPhone 12 Pro Max",
    "data": {
        "color": "Cloudy White",
        "capacity GB": 512
    }
}
