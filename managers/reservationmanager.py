import csv
import datetime
import uuid
from models.hotel import Hotel


class ReservationManager:
    hotels = []

    def __init__(self, name, people, hotel_name, room_number):
        self.name = name
        self.people = people
        self.reservation_id = str(uuid.uuid4().hex)
        self.date = datetime.datetime.now()
        self.hotel_name = hotel_name
        self.room_number = room_number
        self.status = "pending"

    @classmethod
    def load_hotels_from_csv(cls):
        with open('database/hotels.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                hotel = Hotel(row.get('hotel_name'), int(row.get('stars')), row.get('location'))
                cls.hotels.append(hotel)

    @classmethod
    def __find_available_rooms(cls):
        available_rooms = []
        for hotel in cls.hotels:
            for room in hotel.rooms:
                if room.is_available:
                    available_rooms.append(room)
        if len(available_rooms) == 0:
            raise Exception("No rooms available")
        return available_rooms

    @classmethod
    def __find_available_hotels(cls, location):
        return [hotel for hotel in cls.hotels if hotel.location == location]

    @classmethod
    def __find_hotel_instance_by_name(cls, name):
        for hotel in cls.hotels:
            if hotel.hotel_name == name:
                return hotel
        raise Exception(f"Hotel {name} not found")

    @classmethod
    def __search_for_room(cls, location, max_people, price):
        available_hotels = cls.__find_available_hotels(location)
        available_rooms = []
        for hotel in available_hotels:
            for room in hotel.rooms:
                if room.max_people >= max_people and room.price <= price and room.is_available:
                    available_rooms.append(room)
        return available_rooms

    @staticmethod
    def add_reservation(hotel, name, people, hotel_name, room_number):
        reservation = ReservationManager(name, people, hotel_name, room_number)
        hotel.reservations.append(reservation)
        return reservation

    @classmethod
    def make_reservation(cls):
        name = input("Name: ")
        location = input("Where are you going? ")
        max_people = int(input("How many people are you going to bring? "))
        price = int(input("How much do you want to spend? "))
        rooms = cls.__search_for_room(location, max_people, price)
        if not rooms:
            raise Exception(f"No rooms found in {location} with {max_people} people and {price} EUR")
        for room in rooms:
            print(room)
        room_number = input("Which room do you want to reserve? ")
        for room in rooms:
            if room.room_number == room_number:
                room.is_available = False
                cls.add_reservation(cls.__find_hotel_instance_by_name(room.hotel_name), name,
                                    max_people, room.hotel_name,
                                    room.room_number)
                print(f"You have reserved {room.room_number} in {room.hotel_name}")
                return
        raise Exception(f"Room {room_number} is not available")

    @classmethod
    def get_all_reservations(cls):
        return [reservation for hotel in cls.hotels for reservation in hotel.reservations]

    def __repr__(self):
        return f"{self.name} - {self.people} - {self.reservation_id} - {self.date} - {self.hotel_name} - {self.room_number} - {self.status} "
