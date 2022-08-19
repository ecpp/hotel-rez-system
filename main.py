from managers.reservationmanager import ReservationManager

if __name__ == '__main__':
    ReservationManager.load_hotels_from_csv()

    while True:
        ReservationManager.make_reservation()
        print(ReservationManager.get_all_reservations())
