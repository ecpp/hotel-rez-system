class HotelRoom:
    def __init__(self, hotel_name: str, room_number: str, price: float, max_people: int,
                 is_available: bool):
        assert hotel_name is not None, "Hotel name must be provided!"
        assert room_number.isdigit(), "Room number must be a number!"
        assert price > 0, "Price must be greater than zero!"
        assert max_people > 0, "Max people must be greater than zero!"

        self.hotel_name = hotel_name
        self.room_number = room_number
        self.max_people = max_people
        self.price = price
        self.is_available = is_available

    def __repr__(self):
        return f"Room {self.room_number} costs {self.price} EUR"
