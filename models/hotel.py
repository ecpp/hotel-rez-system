import csv
from models.hotelrooms import HotelRoom


class Hotel:

    def __init__(self, hotel_name: str, stars: int, location: str):
        assert stars >= 0, "Stars must be greater or equal to zero!"
        assert stars <= 5, "Stars must be less or equal to five!"
        assert len(hotel_name) > 0, "Name must be greater than zero!"
        assert len(location) > 0, "Location must be greater than zero!"

        self.hotel_name = hotel_name
        self.stars = stars
        self.location = location
        self.rooms = []
        self.reservations = []
        Hotel.__load_rooms_from_csv(self)

    def __load_rooms_from_csv(self):
        with open('database/rooms.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                room = HotelRoom(row.get('hotel_name'), row.get('room_number'), float(row.get('price'))
                                 , int(row.get('max_people')), bool(row.get('is_available')))
                if room.hotel_name == self.hotel_name:
                    self.rooms.append(room)

    def __repr__(self):
        return f"{self.hotel_name} has {self.stars} stars and is located in {self.location}"
