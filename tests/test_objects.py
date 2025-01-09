from src.get_object import GetObject


class TestObjects:
    def test_get_object(self):
       object = GetObject().get_object()
       assert object["id"] == "3"
       assert object["name"] == "Apple iPhone 12 Pro Max"
       assert object["data"]["color"] == "Cloudy White"
       assert object["data"]["capacity GB"] == 512
