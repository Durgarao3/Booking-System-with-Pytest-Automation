# booking.py

class BookingSystem:
    def __init__(self):
        self.bookings = []  # stores bookings as tuples (name, slot)

    def book(self, name, slot):
        if any(s == slot for _, s in self.bookings):
            raise ValueError("Slot already booked")
        self.bookings.append((name, slot))
        return True

    def cancel(self, name, slot):
        if (name, slot) not in self.bookings:
            raise ValueError("No such booking found")
        self.bookings.remove((name, slot))
        return True

    def list_bookings(self):
        return self.bookings

    def is_slot_available(self, slot):
        return not any(s == slot for _, s in self.bookings)
